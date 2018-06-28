from functools import lru_cache
class Solution:
    @lru_cache(maxsize=32)
    def climbStairs(self, n):
        if n < 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
