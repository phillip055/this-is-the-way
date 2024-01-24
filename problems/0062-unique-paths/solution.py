class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def helper(m, n):
            if n < 0 or m < 0:
                return 0
            if n == 0 and m == 0:
                return 1
            return (
                helper(m - 1, n) +
                helper(m, n - 1)
            )
        return helper(m-1, n-1)
