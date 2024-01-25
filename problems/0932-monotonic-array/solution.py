class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        for idx in range(1, len(nums)):
            diff = nums[idx] - nums[idx-1]
            if diff == 0:
                continue
            elif diff > 0:
                decreasing = False
            else:
                increasing = False
        return increasing or decreasing


