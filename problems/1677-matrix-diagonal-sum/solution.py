class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        for i in range(len(mat)):
            _sum += mat[i][i]
            _sum += mat[i][len(mat)-1-i]
        if len(mat) % 2 != 0:
            _sum -= mat[(len(mat)-1)//2][(len(mat)-1)//2]
        return _sum

