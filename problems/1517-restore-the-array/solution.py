class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = {}
        mod = 10 ** 9 + 7
        def rec(idx0):
            if idx0 in dp:
                return dp[idx0]
            if len(s) == idx0:
                return 1
            if s[idx0] == '0':
                return 0
            result = 0
            for idx1 in range(idx0, len(s)):
                remaining = int(s[idx0: idx1 + 1])
                if remaining > k:
                    break
                result += rec(idx1+1)
            dp[idx0] = result % mod
            return result
        
        return rec(0) % mod

