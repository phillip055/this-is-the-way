class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx0, idx1 = 0, len(nums)
        while idx0 < idx1:
            if nums[idx0] == val:
                nums[idx0] = nums[idx1 - 1]
                idx1 -= 1
                continue
            idx0 += 1
        return idx1
