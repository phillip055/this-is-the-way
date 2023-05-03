class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one, two = set(nums1), set(nums2)
        return list(one.difference(two)), list(two.difference(one))
