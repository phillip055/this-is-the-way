class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        idx0, idx1 = 0, len(nums) - 1
        while idx0 <= idx1:
            if abs(nums[idx0]) > abs(nums[idx1]):
                result.append(pow(nums[idx0],2))
                idx0 += 1
            else:
                result.append(pow(nums[idx1],2))
                idx1 -= 1
        return list(reversed(result))
