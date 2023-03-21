class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        currIdx = 0
        result = 0
        while currIdx < len(nums):
            if nums[currIdx] == 0:
                startIdx = currIdx
                endIdx = currIdx
                while endIdx < len(nums) and nums[endIdx] == 0:
                    result += endIdx - startIdx + 1
                    endIdx += 1
                currIdx = endIdx
            else:
                currIdx += 1
        return result
                
