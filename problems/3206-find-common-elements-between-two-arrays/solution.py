class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_set = set(nums2)
        nums1_set = set(nums1)
        left = 0
        right = 0
        for num1 in nums1:
            if num1 in nums2_set:
                left += 1
        for num2 in nums2:
            if num2 in nums1_set:
                right += 1
    
        return [left, right]

