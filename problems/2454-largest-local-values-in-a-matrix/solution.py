class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = [[0 for _ in range(len(grid)-2)] for _ in range(len(grid)-2)]
        for x in range(len(grid)-2): 
            for y in range(len(grid)-2):
                _max = float("-inf")
                for _x in range(x, x+3):
                    for _y in range(y, y+3):
                        _max = max(grid[_x][_y], _max)
                answer[x][y] = _max
        return answer

