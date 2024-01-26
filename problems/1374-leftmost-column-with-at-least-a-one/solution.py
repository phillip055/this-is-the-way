# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        num_rows, num_cols = binaryMatrix.dimensions()
        
        ans = float('inf')
        for rowIdx in range(num_rows):
            l, r = 0, num_cols - 1
            while l <= r:
                mid = (r+l) // 2
                mid_val = binaryMatrix.get(rowIdx, mid)
                if mid_val == 1:
                    ans = min(ans, mid)
                    if mid - 1 >= 0 and binaryMatrix.get(rowIdx, mid - 1) == 0:
                        break
                if mid_val == 1:
                    r = mid - 1
                else:
                    l = mid + 1
        return ans if ans != float('inf') else -1

