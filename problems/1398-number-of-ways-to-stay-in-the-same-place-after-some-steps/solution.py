class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7   
        @cache
        def helper(idx, steps, arrayLen):
            if idx >= arrLen or idx < 0:
                return 0
            if steps == 0 and idx == 0:
                return 1
            if steps == 0:
                return 0
            result = 0
            result += helper(idx + 1, steps - 1, arrLen) % MOD
            result += helper(idx - 1, steps - 1, arrLen) % MOD
            result += helper(idx, steps - 1, arrLen)
            return result
        return helper(0, steps, arrLen) % MOD

