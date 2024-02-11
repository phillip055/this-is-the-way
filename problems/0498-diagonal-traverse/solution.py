class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        def goDiagonal(rowIdx, colIdx):
            if rowIdx < 0 or colIdx > len(mat[0]) - 1:
                return
            result.append(mat[rowIdx][colIdx])
            goDiagonal(rowIdx - 1, colIdx + 1)
        
        for row in range(len(mat)):
            result = []
            goDiagonal(row, 0)
            res.append(result)
        
        for col in range(1, len(mat[0])):
            result = []
            goDiagonal(len(mat) - 1, col)
            res.append(result)
        
        output = []
        for idx, d in enumerate(res):
            if idx % 2 == 0:
                output.extend(d)
            else:
                output.extend(d[::-1])
        return output

