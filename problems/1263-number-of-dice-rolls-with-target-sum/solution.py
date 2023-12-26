class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n or target > n * k:
            return 0        
        if n == 0 or target == n * k:
            return 1
        re = 0
        for roll in range(1, k + 1):
            re += self.numRollsToTarget(n - 1, k, target - roll)
        return re % (10**9 + 7)
        
