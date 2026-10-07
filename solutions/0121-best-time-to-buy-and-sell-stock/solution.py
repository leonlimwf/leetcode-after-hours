class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        cheapest = float("inf")
        for price in prices:
            profit = max(profit, price-cheapest)
            cheapest = min(price, cheapest)
        return profit
