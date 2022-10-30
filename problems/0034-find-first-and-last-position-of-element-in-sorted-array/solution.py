class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target, start=0, end=len(nums)-1):
            if end < start:
                return -1
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(nums, target, start, mid-1)
            else:
                return binarySearch(nums, target, mid+1, end)
        
        
        idx = binarySearch(nums, target)
        first, last = idx, idx
        while first - 1 >= 0 and nums[first - 1] == target:
            first -= 1
        while last + 1 < len(nums) and nums[last + 1] == target:
            last += 1
        return first, last
        # start, end = 0, len(nums) - 1
        # while start <= end:
        #     print(start, end)
        #     mid = (end + start) // 2
        #     print(mid)
        #     val = nums[mid]
        #     if val == target:
        #         first = mid
        #         last = mid
        
        #         return first, last
        #     elif val > target:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
        # return -1,-1

