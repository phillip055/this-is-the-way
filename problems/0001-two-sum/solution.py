class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        finding = {}
        for idx, num in enumerate(nums):
            if num in finding:
                return finding[num], idx
            finding[target - num] = idx
        return False

