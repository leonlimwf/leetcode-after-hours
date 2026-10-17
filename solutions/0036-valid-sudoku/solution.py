class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                box = (r//3)*3+(c//3)

                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
        return True
