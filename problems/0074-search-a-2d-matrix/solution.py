class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, (len(matrix) * len(matrix[0])) - 1

        while start <= end:
            mid = start + (end - start // 2)
            row, col = divmod(mid, len(matrix[0]))
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


