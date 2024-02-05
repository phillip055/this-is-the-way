# Algorithm
# [1,2,3,4]
# prefix_list = [1, 1, 2, 6]
# suffix_list = [24, 12, 4, 1]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) # [1, 1,1,1]
        suffix = [1] * len(nums) # [1, 1,1,1]
        n = len(nums) - 1
        for idx in range(1, len(nums)): #idx=1
            prefix[idx] = prefix[idx-1]*nums[idx-1]
            suffix[n - idx] = suffix[n - idx + 1] * nums[n - idx + 1]
        
        return [p * s for p, s in zip(prefix, suffix)]
            


