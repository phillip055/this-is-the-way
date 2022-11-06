from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def rec(i):
            if i < 0:
                return 0
            
            return max(rec(i-1), rec(i-2) + nums[i])
        
        return rec(len(nums) - 1)

