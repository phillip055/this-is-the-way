class Solution:
    def search(self, nums: List[int], target: int) -> int:
        firstIdx = 0
        lastIdx = len(nums) - 1
        while firstIdx <= lastIdx:
            mid = firstIdx + (lastIdx - firstIdx) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                lastIdx = mid - 1
            else:
                firstIdx = mid + 1
        return -1
