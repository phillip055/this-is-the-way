class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = r = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if nums[l] != target:
            return [-1,-1]

        while l - 1 >= 0 and nums[l-1] == target:
            l -= 1
        while r + 1 <= len(nums) - 1 and nums[r+1] == target:
            r += 1
        return [l, r]
        

