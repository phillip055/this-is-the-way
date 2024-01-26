class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        for idx in range(1, len(nums)):
            prefix[idx] = nums[idx-1] * prefix[idx-1]
            suffix[len(nums) - 1 - idx] = suffix[len(nums) - 1 - idx + 1] * nums[len(nums) - 1 - idx + 1]
        
        result = []
        for p, s in zip(prefix, suffix):
            result.append(p*s)
        return result
        
        
            
        
