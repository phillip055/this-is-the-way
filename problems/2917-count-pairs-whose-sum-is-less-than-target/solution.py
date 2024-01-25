class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        idx0, idx1 = 0, len(nums) - 1
        count = 0
        while idx0 < idx1:
            if nums[idx0] + nums[idx1] < target:
                count += idx1 - idx0
                idx0 +=1
            else:
                idx1 -= 1
        return count

