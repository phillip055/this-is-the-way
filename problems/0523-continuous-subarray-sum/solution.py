class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            r = curr_sum % k
            if r not in remainder:
                remainder[r] = idx
            elif idx - remainder[r] > 1:
                return True

