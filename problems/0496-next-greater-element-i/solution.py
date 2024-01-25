class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        
        stack = [nums2[0]]
        for idx in range(len(nums2)):
            while len(stack) and nums2[idx] > stack[-1]:
                result[stack.pop()] = nums2[idx]
            stack.append(nums2[idx])
        
        res = len(nums1) * [-1]
        for idx,num in enumerate(nums1):
            if num in result:
                res[idx] = result[num]
        return res

