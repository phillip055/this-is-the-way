class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        prev = nums[0]
        result = 1
        curr = 1
        for idx in range(1, len(nums)):
            if nums[idx] > prev:
                curr += 1
            else:
                curr = 1
            result = max(curr, result)
            prev = nums[idx]
        return result

