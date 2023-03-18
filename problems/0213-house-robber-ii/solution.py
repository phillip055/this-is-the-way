from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def rec(i, haveFirst=False):
            if haveFirst and i == len(nums)-1:
                return 0
            if i > len(nums) - 1:
                return 0
            if i == 0:
                return max(nums[i] + rec(i+2, haveFirst=True), rec(i+1))
            return max(nums[i] + rec(i+2, haveFirst), rec(i+1, haveFirst))
        return rec(0)

