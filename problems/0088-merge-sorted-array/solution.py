class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_to_insert = len(nums1) - 1
        idx1, idx2 = m - 1, len(nums2) - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[idx_to_insert] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idx_to_insert] = nums2[idx2]
                idx2 -= 1
            idx_to_insert -= 1
        
        while idx1 >= 0:
            nums1[idx_to_insert] = nums1[idx1]
            idx1 -= 1
            idx_to_insert -= 1
        
        while idx2 >= 0:
            nums1[idx_to_insert] = nums2[idx2]
            idx2 -= 1
            idx_to_insert -= 1

