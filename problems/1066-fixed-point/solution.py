class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        for idx, num in enumerate(arr):
            if idx == num:
                return idx
        return -1
