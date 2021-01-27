class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [n for n in set(nums1) & set(nums2) for i in range(min(nums1.count(n), nums2.count(n)))]
                    
