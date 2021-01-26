class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = range(1, len(nums) + 1)
        n = set(nums)
        return [sum(nums) - sum(n), sum(m) - sum(n)]
