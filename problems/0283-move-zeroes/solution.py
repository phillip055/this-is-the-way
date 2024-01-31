class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_of_zeroes = 0
        for num in nums:
            if num == 0:
                count_of_zeroes += 1
        
        idx = 0
        for num in nums:
            if num != 0:
                nums[idx] = num
                idx += 1
        
        for idx in range(len(nums) - count_of_zeroes, len(nums)):
            nums[idx] = 0    
        
