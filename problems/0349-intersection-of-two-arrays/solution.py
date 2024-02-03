class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = set(nums1)
        result = set()
        for num in nums2:
            if num in n:
                result.add(num)
        return result
