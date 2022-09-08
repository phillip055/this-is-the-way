class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        accLeftSum = 0
        for i in range(len(nums)):
            accLeftSum += nums[i]
            leftSum = accLeftSum - nums[i]
            rightSum = totalSum - accLeftSum
            if rightSum == leftSum:
                return i
        return -1
