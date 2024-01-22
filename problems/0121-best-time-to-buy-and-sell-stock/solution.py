class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit, 0)
            min_price = min(min_price, price)
        return max_profit

