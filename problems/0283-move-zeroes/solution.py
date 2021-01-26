class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        for i in nums:
            if i==0:
                nums.remove(i)
                zero=i
                nums.append(zero)
