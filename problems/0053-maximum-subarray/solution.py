class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalMax = float('-inf')
        currentMax = float('-inf')
        
        for num in nums:
            if (num > currentMax + num):
                currentMax = num
            else:
                currentMax += num
            totalMax = max(totalMax, currentMax)
        return totalMax
