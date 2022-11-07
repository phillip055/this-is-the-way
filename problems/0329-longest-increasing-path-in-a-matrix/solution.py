from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        @cache
        def dfs(i, j, prev):
            if i < 0 or i > len(matrix) - 1:
                return 0
            if j < 0 or j > len(matrix[0]) - 1:
                return 0
            if matrix[i][j] > prev:
                left = dfs(i, j-1, matrix[i][j])
                right = dfs(i, j+1, matrix[i][j])
                up = dfs(i - 1, j, matrix[i][j])
                down = dfs(i + 1, j, matrix[i][j])
                return 1 + max(left, right, up, down)
            else:
                return 0
            
        _max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                _max = max(dfs(i,j, float('-inf')), _max)
        return _max
