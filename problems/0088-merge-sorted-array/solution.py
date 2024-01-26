class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx = len(nums1) - 1
        idx0, idx1 = m-1, n-1
        while idx0 >= 0 and idx1 >= 0:
            if nums1[idx0] > nums2[idx1]:
                nums1[idx] = nums1[idx0]
                idx0 -= 1
            else:
                nums1[idx] = nums2[idx1]
                idx1 -= 1
            idx -= 1

        while idx1 >= 0:
            nums1[idx1] = nums2[idx1]
            idx1 -= 1
        return nums1
        
