class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        
        for i in prices:
            if i < minPrice:
                minPrice = i
            else:
                maxProfit = max(maxProfit, i - minPrice)
        
        return maxProfit
        
        
