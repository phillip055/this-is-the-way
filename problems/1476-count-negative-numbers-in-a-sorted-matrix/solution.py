class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        for row in grid:
            _len = len(row)
            for item in row:
                if item < 0:
                    break
                _len -= 1
            negatives += _len
        return negatives

