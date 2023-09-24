class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows = [[0] * k for k in range(1, 102)]
        rows[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                overflow = (rows[row][col] - 1.0) / 2.0
                if overflow > 0:
                    rows[row+1][col] += overflow
                    rows[row+1][col+1] += overflow
        return min(1, rows[query_row][query_glass])
        
