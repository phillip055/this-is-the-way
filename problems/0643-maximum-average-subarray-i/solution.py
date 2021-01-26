class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = result = sum(nums[0 : k])
        for i in range(len(nums) - k):
            cur += nums[i + k] - nums[i]
            result = max(cur, result)
        return float(result) / k
