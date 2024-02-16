class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) <= 1:
            return True
        
        for row in range(1, len(matrix)):
            if matrix[row-1][:-1] != matrix[row][1:]:
                return False
        return True


