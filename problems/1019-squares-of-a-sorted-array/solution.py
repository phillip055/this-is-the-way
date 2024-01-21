class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx0, idx1 = 0, len(nums) - 1
        result = []
        while idx0 <= idx1:
            if abs(nums[idx0]) < abs(nums[idx1]):
                nums[idx1] = nums[idx1] ** 2
                result.append(nums[idx1])
                idx1 -= 1
            else:
                nums[idx0] = nums[idx0] ** 2
                result.append(nums[idx0])
                idx0 += 1
        return list(reversed(result))


