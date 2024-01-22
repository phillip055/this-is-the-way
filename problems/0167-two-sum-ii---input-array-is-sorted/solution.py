class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx0, idx1 = 0, len(nums) - 1
        while idx0 < idx1:
            val = nums[idx0] + nums[idx1]
            if target == val:
                return [idx0 + 1, idx1 + 1]
            elif target < val:
                idx1 -= 1
            else:
                idx0 += 1
        return [-1,-1]
    
