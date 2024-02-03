[0,0]
0

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not len(nums):
            return [[lower, upper]]
        nums.sort()
        result = []

        for idx in range(1, len(nums)):
            if nums[idx-1] + 1 < nums[idx]:
                result.append([nums[idx-1] + 1, nums[idx] - 1])
        
        if nums[0] > lower:
            result = [[lower, nums[0]-1]] + result
        
        if nums[-1] < upper:
            result = result + [[nums[-1] + 1, upper]]
        return result




