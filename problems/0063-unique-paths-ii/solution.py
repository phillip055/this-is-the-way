from functools import cache

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        @cache
        def helper(x, y):
            if x == -1 or y == -1:
                return 0
            if x >= len(grid[0]) or y >= len(grid):
                return 0
            if grid[y][x] == 1:
                return 0
            if x == len(grid[0]) -1 and y == len(grid) - 1:
                return 1
            
            return helper(x + 1, y) + helper(x, y + 1)

        return helper(0, 0)
