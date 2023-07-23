class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for idx in range(1, len(nums)):
            result.append(result[-1] + nums[idx])
        return result
            
