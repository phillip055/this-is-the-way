class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        total = 0

        def helper(rowIdx, colIdx):
            if rowIdx >= len(grid) or colIdx >= len(grid[0]):
                return 0
            if rowIdx < 0 or colIdx < 0:
                return 0
            if grid[rowIdx][colIdx] == 0:
                return 0
            
            ov = grid[rowIdx][colIdx]
            grid[rowIdx][colIdx] = 0

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            _s = 0

            for direction in directions:
                _s = max(helper(rowIdx + direction[0], colIdx + direction[1]), _s)
            
            grid[rowIdx][colIdx] = ov
            return _s + ov
        
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                # print("start", rowIdx, colIdx)
                total = max(helper(rowIdx, colIdx), total)
        return total

                
            

