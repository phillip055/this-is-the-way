class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0
        for num in nums:
            if num != 0:
                nums[non_zero_idx] = num
                non_zero_idx += 1
        for idx in range(non_zero_idx, len(nums)):
            nums[idx] = 0
        
