class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]
        for rowIdx in range(9):
            for colIdx in range(9):
                val = board[rowIdx][colIdx]
                if val == ".":
                    continue
                if val in rowSets[rowIdx] or val in colSets[colIdx] or val in boxSets[rowIdx//3][colIdx//3]:
                    return False
                boxSets[rowIdx//3][colIdx//3].add(val)
                rowSets[rowIdx].add(val)
                colSets[colIdx].add(val)
        return True
