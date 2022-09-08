class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        totalScore = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    totalScore += 4
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        totalScore -= 2
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        totalScore -= 2
        return totalScore
