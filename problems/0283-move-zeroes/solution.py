class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        non_zero = 0
        for num in nums:
            if num != 0:
                nums[non_zero] = num
                non_zero += 1
        
        for idx in range(non_zero, len(nums)):
            nums[idx] = 0
        return nums

