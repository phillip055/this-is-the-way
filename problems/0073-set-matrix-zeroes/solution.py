class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = set()
        cols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows:
                    matrix[i][j] = 0
                    continue
                if j in cols:
                    matrix[i][j] = 0
                    continue
        
        return matrix
                
