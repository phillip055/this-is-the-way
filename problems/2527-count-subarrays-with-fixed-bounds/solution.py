class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        startIdx = -1
        lastMinIdx = -1
        lastMaxIdx = -1

        count = 0

        for i in range(len(nums)):
            if nums[i] >= minK and nums[i] <= maxK:
                if nums[i] == minK:
                    lastMinIdx = i
                if nums[i] == maxK:
                    lastMaxIdx = i
                count += max(0, min(lastMinIdx, lastMaxIdx)-startIdx)
            else:
                lastMinIdx = -1
                lastMaxIdx = -1
                startIdx = i
        return count

