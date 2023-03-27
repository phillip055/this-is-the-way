from functools import cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @cache
        def dfs(x, y):
            if x >= len(grid[0]) or y >= len(grid):
                return float('inf')
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                return grid[y][x]
            return grid[y][x] + min(
                dfs(x, y+1),
                dfs(x+1, y),
            )

        return dfs(0,0)

