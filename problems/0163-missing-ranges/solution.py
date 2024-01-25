

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        missing = []
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx-1] > 1:
                missing.append([nums[idx-1] + 1, nums[idx] - 1])
        if lower < nums[0]:
            missing = [[lower, nums[0] - 1]] + missing
        
        if upper > nums[-1]:
            missing = missing + [[nums[-1] + 1, upper]]
        return missing

