class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - 1 < 0 or j - 1 < 0:
                    continue
                if matrix[i][j] != matrix[i - 1][j-1]:
                    return False
        return True
            
