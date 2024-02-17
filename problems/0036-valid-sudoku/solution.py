class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in board]
        colSets = [set() for _ in board[0]]
        boxSets = [[set() for _ in range(3)] for _ in range(3)]

        for rowIdx in range(9):
            for colIdx in range(9):
                ele = board[rowIdx][colIdx]
                if ele == ".":
                    continue
                if ele in rowSets[rowIdx]:
                    return False
                if ele in colSets[colIdx]:
                    return False
                if ele in boxSets[rowIdx//3][colIdx//3]:
                    return False
                rowSets[rowIdx].add(ele)
                colSets[colIdx].add(ele)
                boxSets[rowIdx//3][colIdx//3].add(ele)
        return True

