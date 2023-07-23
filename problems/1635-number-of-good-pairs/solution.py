class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for indi, i in enumerate(nums):
            for j in nums[indi+1:]:
                if i == j:
                    counter += 1
        return counter
