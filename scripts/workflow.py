#!/usr/bin/env python3
"""Read-only coach preflight: due phase, no-repeat inventory, and actual journal code."""

import argparse
from datetime import datetime, time, timedelta
import hashlib
import json
from pathlib import Path
import random
import re
import sys
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

from sync import journal_entries, section, sha256, solution_code, sync_lock

SGT = ZoneInfo("Asia/Singapore")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def due_slot(timestamp, phase="auto", date=None):
    moment = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    if moment.tzinfo is None:
        raise ValueError("A timezone-qualified trigger timestamp is required.")
    local = moment.astimezone(SGT)
    if phase != "auto":
        intended_date = datetime.fromisoformat(date).date() if date else local.date()
        if phase == "midnight" and not date and local.hour == 23 and local.minute >= 50:
            intended_date += timedelta(days=1)
        slot = datetime.combine(intended_date, time(0 if phase == "midnight" else 5), SGT)
    else:
        # Allow ten minutes early; otherwise resolve the most recent scheduled slot.
        # No upper lateness window: delayed heartbeat delivery must still execute.
        cutoff = local + timedelta(minutes=10)
        candidates = [datetime.combine(local.date() + timedelta(days=offset), time(hour), SGT)
                      for offset in (-1, 0, 1) for hour in (0, 5)]
        slot = max(candidate for candidate in candidates if candidate <= cutoff)
        phase = "midnight" if slot.hour == 0 else "check"
    return {"phase": phase, "date": slot.date().isoformat(), "scheduled_at": slot.isoformat(),
            "triggered_at": local.isoformat(), "lateness_seconds": int((local - slot).total_seconds())}


def used_slugs(ledger):
    """Union all durable solved/assigned history, including screenshot slug lists."""
    found = set()

    def walk(value, list_of_slugs=False):
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"slug", "titleSlug", "assigned_slug"} and isinstance(child, str) and SLUG.fullmatch(child):
                    found.add(child)
                else:
                    walk(child, "slug" in key or key == "recent_accepted_in_screenshot")
        elif isinstance(value, list):
            for child in value:
                walk(child, list_of_slugs)
        elif list_of_slugs and isinstance(value, str) and SLUG.fullmatch(value):
            found.add(value)

    for key in ("assigned", "accepted", "skipped", "profile", "observed_progress", "solved_history"):
        value = ledger.get(key, [])
        walk(value, key in {"accepted", "skipped", "solved_history"})
    return sorted(found)


def inspect_entry(lines):
    work = section(lines, "First Instinct", {"Complexity Analysis", "Completion Check"})
    analysis = "\n".join(section(lines, "Complexity Analysis", {"Completion Check"})).strip()
    try:
        code = solution_code(lines)
        outcome = "python_found" if code else "no_python_found"
    except (SyntaxError, ValueError):
        code = None
        outcome = "invalid_or_ambiguous_python"
    return {"code_outcome": outcome, "code": code,
            "code_sha256": hashlib.sha256(code.encode()).hexdigest() if code else None,
            "learner_work": work,
            "learner_work_sha256": hashlib.sha256(json.dumps(work, ensure_ascii=False).encode()).hexdigest(),
            "complexity": analysis or None,
            "complexity_sha256": hashlib.sha256(analysis.encode()).hexdigest() if analysis else None}


def preflight(ledger_path, journal_path, slot, slug=None):
    ledger = json.loads(ledger_path.read_text())
    assignments = ledger["assigned"]
    if len({a["slug"] for a in assignments}) != len(assignments):
        raise ValueError("Duplicate assignment slug in private ledger.")
    if len({a["number"] for a in assignments}) != len(assignments):
        raise ValueError("Duplicate journal entry number in private ledger.")
    matches = [a for a in assignments if a["slug"] == slug] if slug else [a for a in assignments if a["date"] == slot["date"]]
    if len(matches) > 1:
        raise ValueError("Multiple assignments for the intended date.")
    assignment = matches[0] if matches else None
    entries = journal_entries(journal_path, assignments)
    current_hash = sha256(journal_path)
    baseline = ledger.get("daily_baselines", {}).get(slot["date"])
    if baseline and assignment and not slug and baseline.get("assigned_slug") != assignment["slug"]:
        raise ValueError("Daily baseline refers to a different assignment.")
    checks = [c for c in ledger.get("checks", []) if c.get("date") == slot["date"] and
              (not assignment or c.get("assigned_slug") == assignment["slug"])]
    previous_hash = next((checks[-1].get(key) for key in ("docx_sha256_after_update", "docx_sha256_after_edit", "current_docx_sha256")
                          if checks and checks[-1].get(key)), None)
    summary = []
    for a in assignments:
        entry = inspect_entry(entries[a["slug"]]) if a["slug"] in entries else {"code_outcome": "journal_entry_missing", "complexity": None}
        summary.append({"slug": a["slug"], "leetcode_number": a["leetcode_number"], "status": a["status"],
                        "code_outcome": entry["code_outcome"], "complexity_available": bool(entry["complexity"])})
    return {"slot": slot, "assignment": assignment, "midnight_baseline": baseline,
            "pre_edit_docx_sha256": current_hash,
            "matches_midnight_baseline": current_hash == baseline.get("docx_sha256") if baseline else None,
            "existing_check": checks[-1] if checks else None,
            "matches_previous_checker_output": bool(previous_hash and current_hash == previous_hash),
            "baseline_required_missing": slot["phase"] == "check" and (not assignment or not baseline),
            "entry": inspect_entry(entries[assignment["slug"]]) if assignment and assignment["slug"] in entries else None,
            "used_slugs": used_slugs(ledger), "inventory": summary,
            "confirmed_count": sum(a["status"] == "accepted" for a in assignments)}


def pick(ledger, candidates, date):
    existing = [a for a in ledger["assigned"] if a["date"] == date]
    if len(existing) > 1:
        raise ValueError("Multiple assignments for date.")
    if existing:
        return {"reused": True, "selection": existing[0]}
    used = set(used_slugs(ledger))
    eligible = []
    seen = set()
    for candidate in candidates:
        slug = candidate["slug"]
        if not SLUG.fullmatch(slug):
            raise ValueError("Invalid candidate slug.")
        if candidate.get("difficulty") in {"Easy", "Medium"} and slug not in used and slug not in seen:
            seen.add(slug)
            eligible.append(candidate)
    if not eligible:
        raise ValueError("No fresh Easy or Medium candidates remain.")
    return {"reused": False, "selection": random.SystemRandom().choice(eligible),
            "eligible_count": len(eligible), "must_save_before_retry": True}


def public_profile(username):
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,40}", username):
        raise ValueError("Invalid public handle.")
    query = """query PublicProgress($username: String!, $limit: Int!) {
      matchedUser(username: $username) {
        submitStatsGlobal { acSubmissionNum { difficulty count } }
      }
      recentAcSubmissionList(username: $username, limit: $limit) {
        title titleSlug timestamp
      }
    }"""
    request = Request("https://leetcode.com/graphql/",
                      data=json.dumps({"query": query, "variables": {"username": username, "limit": 20}}).encode(),
                      headers={"Content-Type": "application/json", "User-Agent": "LeetCodeAfterHours/1.0"})
    try:
        with urlopen(request, timeout=15) as response:
            if response.geturl() != "https://leetcode.com/graphql/":
                raise ValueError("Unexpected profile redirect.")
            payload = json.loads(response.read(1024 * 1024))
        data = payload.get("data", {})
        if payload.get("errors") or not data.get("matchedUser") or not isinstance(data.get("recentAcSubmissionList"), list):
            raise ValueError("Public profile response incomplete.")
        recent = []
        for item in data["recentAcSubmissionList"]:
            if not SLUG.fullmatch(item["titleSlug"]):
                raise ValueError("Invalid observed slug.")
            recent.append({"slug": item["titleSlug"], "title": item["title"], "statusDisplay": "Accepted",
                           "submitted_at": datetime.fromtimestamp(int(item["timestamp"]), SGT).isoformat()})
        return {"available": True, "observed_at": datetime.now(SGT).isoformat(timespec="seconds"),
                "source": "Live public LeetCode GraphQL (no login or cookies)",
                "solved_counts": data["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"],
                "recent_accepted": recent, "complete_solved_history": False,
                "learner_acceptance_confirmed": False}
    except (OSError, ValueError, KeyError, TypeError):
        return {"available": False, "browser_fallback_required": True,
                "source": "Public LeetCode lookup unavailable", "learner_acceptance_confirmed": False}


def record_profile(ledger_path, observation):
    """Record only observed progress; never promote a learner status to Accepted."""
    if not observation.get("available"):
        return False
    if ledger_path.is_symlink():
        raise ValueError("Expected a regular private ledger, not a symlink.")
    with sync_lock(ledger_path.parent) as state:
        original_hash = sha256(ledger_path)
        ledger = json.loads(ledger_path.read_text())
        profile = ledger.setdefault("profile", {})
        when = observation["observed_at"]
        source = observation["source"]
        profile.update(last_checked_at=when, checked_on=when[:10], status="public_profile_found")
        counts = {item["difficulty"].lower(): item["count"] for item in observation["solved_counts"]}
        profile.setdefault("stats", {})["accepted"] = counts
        progress = {"observed_at": when, "source": source, "solved_total": counts.get("all"),
                    "recent_accepted_count": len(observation["recent_accepted"])}
        history = profile.setdefault("observed_progress", [])
        if not any(item.get("observed_at") == when and item.get("source") == source for item in history):
            history.append(progress)
        recent = profile.setdefault("recent_accepted", [])
        observed = {item.get("slug", item.get("titleSlug")): item for item in recent if isinstance(item, dict)}
        for item in observation["recent_accepted"]:
            record = dict(item, observed_at=when, observation_source=source)
            if item["slug"] in observed:
                observed[item["slug"]].update(record)
            else:
                recent.append(record)
            for assignment in ledger["assigned"]:
                if assignment["slug"] == item["slug"]:
                    assignment.update(profile_observed_status="Accepted", profile_observed_at=when,
                                      profile_observation_source=source)
        # Preserve baselines, check records, learner statuses and confirmations verbatim.
        temporary = state / "profile-ledger.json"
        if temporary.is_symlink():
            raise ValueError("Unexpected temporary ledger symlink.")
        temporary.touch(mode=0o600, exist_ok=True)
        temporary.chmod(0o600)
        temporary.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n")
        if sha256(ledger_path) != original_hash:
            raise ValueError("Ledger changed while recording observation; retry.")
        temporary.chmod(ledger_path.stat().st_mode & 0o777)
        temporary.replace(ledger_path)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    inspect = commands.add_parser("inspect", help="Private output: do not publish this JSON")
    inspect.add_argument("--ledger", type=Path, required=True)
    inspect.add_argument("--journal", type=Path, required=True)
    inspect.add_argument("--triggered-at", default=datetime.now(SGT).isoformat())
    inspect.add_argument("--phase", choices=["auto", "midnight", "check"], default="auto")
    inspect.add_argument("--date")
    inspect.add_argument("--slug")
    choose = commands.add_parser("pick")
    choose.add_argument("--ledger", type=Path, required=True)
    choose.add_argument("--candidates", type=Path, required=True)
    choose.add_argument("--date", required=True)
    profile = commands.add_parser("profile")
    profile.add_argument("--username", default="leonlimwf")
    profile.add_argument("--ledger", type=Path)
    profile.add_argument("--record", action="store_true", help="Persist public observations only; preserve learner statuses")
    args = parser.parse_args()
    if args.command == "inspect":
        result = preflight(args.ledger, args.journal, due_slot(args.triggered_at, args.phase, args.date), args.slug)
    elif args.command == "pick":
        result = pick(json.loads(args.ledger.read_text()), json.loads(args.candidates.read_text()), args.date)
    else:
        if args.record and not args.ledger:
            parser.error("--record requires --ledger")
        result = public_profile(args.username)
        if args.record:
            result["observation_recorded"] = record_profile(args.ledger, result)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print("Coach preflight failed (" + type(error).__name__ + "); inspect local inputs privately.", file=sys.stderr)
        raise SystemExit(1)
