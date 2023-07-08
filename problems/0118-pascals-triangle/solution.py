class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            row = [1] * i
            for j in range(1, i - 1):
                row[j] = result[i - 2][j] + result[i - 2][j - 1]
            result.append(row)
        return result

