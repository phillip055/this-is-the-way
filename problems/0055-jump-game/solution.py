from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        @cache
        def rec(i):
            if i >= n - 1:
                return True
            
            for e in range(i + 1, min(i + nums[i], n - 1) + 1):
                if rec(e):
                    return True
            return False
        
        return rec(0)
    
