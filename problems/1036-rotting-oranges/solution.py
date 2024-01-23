class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        ready_to_rot = []
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx] == 2:
                    ready_to_rot.append((rowIdx, colIdx))
                if grid[rowIdx][colIdx] == 1:
                    fresh_count += 1
        
        def outside(rowIdx, colIdx):
            return rowIdx < 0 or rowIdx >= len(grid) or colIdx < 0 or colIdx >= len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        while len(ready_to_rot):
            minutes += 1
            for _ in range(len(ready_to_rot)):
                (rowIdx, colIdx) = ready_to_rot.pop(0)
                for direction in directions:
                    nRowIdx = rowIdx + direction[0]
                    nColIdx = colIdx + direction[1]
                    if not outside(nRowIdx, nColIdx):
                        if grid[rowIdx + direction[0]][colIdx + direction[1]] == 1:
                            fresh_count -= 1
                            grid[rowIdx + direction[0]][colIdx + direction[1]] = 2
                            ready_to_rot.append((rowIdx + direction[0], colIdx + direction[1]))
        return max(minutes - 1, 0) if fresh_count == 0 else -1

        
        
