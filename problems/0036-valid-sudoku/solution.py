class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for rowIdx in range(9):
            for colIdx in range(9):
                val = board[rowIdx][colIdx]
                rowBoxIdx = rowIdx // 3
                colBoxIdx = colIdx // 3
                if val == ".":
                     continue
                if val in colSets[colIdx]:
                    return False
                if val in rowSets[rowIdx]:
                    return False
                if val in boxSets[rowBoxIdx][colBoxIdx]:
                    return False
                colSets[colIdx].add(val)
                rowSets[rowIdx].add(val)
                boxSets[rowBoxIdx][colBoxIdx].add(val)
        return True

