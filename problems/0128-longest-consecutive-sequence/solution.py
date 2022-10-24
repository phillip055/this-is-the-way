class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNumbers = set(nums)
        maxLength = 0
        for num in nums:
            curr = 1
            tempNum = num
            while (tempNum - 1) in allNumbers:
                curr += 1
                tempNum -= 1
                allNumbers.remove(tempNum)
            tempNum = num
            while (tempNum + 1) in allNumbers:
                curr += 1
                tempNum += 1
                allNumbers.remove(tempNum)
            maxLength = max(maxLength, curr)
        return maxLength
