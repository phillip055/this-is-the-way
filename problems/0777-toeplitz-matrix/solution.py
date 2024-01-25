class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for rowIdx in range(1, len(matrix)):
            row0 = matrix[rowIdx-1]
            row1 = matrix[rowIdx]
            if row0[:-1] != row1[1:]:
                return False
        return True
            

