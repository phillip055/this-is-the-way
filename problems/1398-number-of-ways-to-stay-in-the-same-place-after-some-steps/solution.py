class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def helper(steps, arrLen, at):
            if steps == 0:
                if at == 0:
                    return 1
                return 0
            count = 0
            count += helper(steps-1, arrLen, at)
            
            if at > 0:
                count = (count + helper(steps-1, arrLen, at-1)) % MOD
        
            if at < arrLen-1:
                count = (count + helper(steps-1, arrLen, at+1)) % MOD
            return count
        
        MOD = 10 ** 9 + 7
        return helper(steps, arrLen, 0)
