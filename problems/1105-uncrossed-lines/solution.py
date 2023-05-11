class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int], answer = 0) -> int:

        @cache
        def helper(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            if nums1[i] == nums2[j]:
                return 1 + helper(i+1, j+1)
            else:
                return max(
                    helper(i+1,j),
                    helper(i,j+1)
                )
            
        return helper(0,0)
        

