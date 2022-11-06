class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            result = -1
            for c in coins:
                if c > i:
                    continue
                dp[i] = min(dp[i], dp[i-c] + 1)
        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1
                
