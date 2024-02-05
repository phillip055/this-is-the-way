# Algorithm
# non_zero_idx = 0

# [0,1,0,3,12]
# [1,1, 0, 3, 12] # non_zero_idx = 1
# [1,3, 0, 3, 12] # non_zero_idx = 2
# [1,3, 12, 3, 12] # non_zero_idx = 3

# ƒor index above and equal 3, 00000


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
        return nums


