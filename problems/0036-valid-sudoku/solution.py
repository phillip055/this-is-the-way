class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSets = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]
        for rowIdx in range(len(board)):
            for colIdx in range(len(board)):
                val = board[rowIdx][colIdx]
                rowBox = rowIdx // 3
                colBox = colIdx // 3
                if val == ".":
                    continue
                if val in colSets[colIdx]:
                    return False
                if val in rowSets[rowIdx]:
                    return False
                if val in boxSets[rowBox][colBox]:
                    return False
                colSets[colIdx].add(val)
                rowSets[rowIdx].add(val)
                boxSets[rowBox][colBox].add(val)
        return True
