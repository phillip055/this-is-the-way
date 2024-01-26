class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        def sort(rowIdx, colIdx):
            arr = []
            rIdx, cIdx = rowIdx, colIdx
            while rIdx <= len(mat) - 1 and cIdx <= len(mat[0]) - 1:
                arr.append(mat[rIdx][cIdx])
                rIdx += 1
                cIdx += 1
            arr = list(sorted(arr))
            idx = 0
            while rowIdx <= len(mat) - 1 and colIdx <= len(mat[0]) - 1:
                mat[rowIdx][colIdx] = arr[idx]
                rowIdx += 1
                colIdx += 1
                idx += 1
            
        
        # row = 0
        for colIdx in range(len(mat[0])):
            sort(0, colIdx)
        for rowIdx in range(1, len(mat)):
            sort(rowIdx, 0)
        return mat
