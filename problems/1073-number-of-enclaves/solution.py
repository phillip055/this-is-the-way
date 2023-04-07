class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i,j):
            if i == -1 or j == -1 or i == rows or j  ==  cols or grid[i][j] == 0:
                return 
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or rows-1 == i or cols-1 == j) and grid[i][j] == 1:
                    dfs(i,j)
        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans += grid[i][j]
        return ans
