class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums, l, r):
            if l == r:
                return l
            mid = (l + r) //2
            if nums[mid] > nums[mid + 1]:
                return search(nums, l, mid)
            return search(nums, mid + 1, r)
        
        return search(nums, 0, len(nums) - 1)
