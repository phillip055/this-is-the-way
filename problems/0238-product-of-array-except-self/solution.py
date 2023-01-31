class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        left_product = 1
        right_product = 1
        for i in range(n):
            output[i] *= left_product
            left_product *= nums[i]
            output[n - 1 - i] *= right_product
            right_product *= nums[n - 1 - i]
        return output

