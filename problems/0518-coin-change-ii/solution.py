class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def helper(amount, idx):
            if amount == 0:
                return 1
            if idx == len(coins):
                return 0
            
            x = 0
            if coins[idx]<=amount:
                x = helper(amount-coins[idx], idx)

            y = helper(amount, idx+1)

            return x + y
        
        return helper(amount, 0)

