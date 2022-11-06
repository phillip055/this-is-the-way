from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        @cache
        def rec(m, n):
            if m == 0 or n == 0:
                return 1
            return rec(m-1, n) + rec(m, n-1)
        
        return rec(m-1, n-1)

