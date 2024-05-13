class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        cols, rows = len(grid[0]), len(grid)
        for rowIdx in range(rows):
            colIdx = 0
            flip = True
            if grid[rowIdx][colIdx] == 1:
                flip = False
            if flip:
                for colIdx in range(cols):
                    if grid[rowIdx][colIdx] == 1:
                        grid[rowIdx][colIdx] = 0
                    else:
                        grid[rowIdx][colIdx] = 1

        for colIdx in range(1, cols):
            threshold = len(grid) // 2
            count = 0
            for rowIdx in range(rows):
                if grid[rowIdx][colIdx] == 1:
                    count += 1
            if count > threshold:
                continue
            for rowIdx in range(rows):
                if grid[rowIdx][colIdx] == 1:
                    grid[rowIdx][colIdx] = 0
                else:
                    grid[rowIdx][colIdx] = 1
        result = 0
        for row in grid:
            row = map(str, row)
            result += int("".join(row), 2)
        return result

