class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs(rowIdx, colIdx):
            to_explore = [(rowIdx, colIdx)]
            visited = set()
            directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
            visited.add((rowIdx, colIdx))
            while len(to_explore):
                rowIdx, colIdx = to_explore.pop(0)
                for direction in directions:
                    nRowIdx = rowIdx + direction[0]
                    if nRowIdx < 0 or nRowIdx > len(grid) - 1:
                        continue
                    nColIdx = colIdx + direction[1]
                    if nColIdx < 0 or nColIdx > len(grid[0]) - 1:
                        continue
                    if grid[nRowIdx][nColIdx] != 1:
                        continue
                    if (nRowIdx, nColIdx) not in visited:
                        to_explore.append((nRowIdx, nColIdx))
                        visited.add((nRowIdx, nColIdx))
            for (rowIdx, colIdx) in visited:
                grid[rowIdx][colIdx] = 0
            return len(visited)

        max_size = 0
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx] == 1:
                    max_size = max(
                        bfs(rowIdx, colIdx),
                        max_size
                    )
        return max_size
        
