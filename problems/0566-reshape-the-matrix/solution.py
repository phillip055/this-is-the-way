class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix=[]
        one_row=[]
        for i in nums:
            for j in i:
                one_row.append(j)
        if r*c == len(one_row):
            for i in range(0,len(one_row),c):
                matrix.append(one_row[i:i+c])
            return matrix
        else:
            return nums
