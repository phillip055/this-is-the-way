class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        print(result)
        for rowIdx in range(len(mat1)):
            for colIdx in range(len(mat2[0])):
                total = 0
                for ele in range(len(mat2)):
                    total += mat1[rowIdx][ele] * mat2[ele][colIdx]
                result[rowIdx][colIdx] = total
        return result
