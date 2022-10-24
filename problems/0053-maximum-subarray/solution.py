class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [nums[0]]
        for idx in range(1, len(nums)):
            num = nums[idx]
            res.append(max(res[-1] + num, num))
        return max(res)
