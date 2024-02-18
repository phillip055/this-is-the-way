class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        max_sum = float('-inf')
        for num in nums:
            curr += num
            curr = max(curr, num)
            max_sum = max(curr, max_sum)
        return max_sum

