class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        currSum = nums[0]
        currSize = 1
        otherSize = len(nums) - 1
        otherSum = sum(nums) - nums[0]
        
        def calculate(currSum, currSize, otherSum, otherSize):
            if otherSize == 0:
                otherSize = 1
            return abs(currSum / currSize - otherSum / otherSize)
        
        result = calculate(currSum, currSize, otherSum, otherSize)
        resultIdx = 0
        for idx in range(1, len(nums)):
            currSum += nums[idx]
            currSize += 1
            otherSum -= nums[idx]
            otherSize -= 1
            candidate = calculate(currSum, currSize, otherSum, otherSize)
            if candidate < result:
                result = candidate
                resultIdx = idx
        return resultIdx
