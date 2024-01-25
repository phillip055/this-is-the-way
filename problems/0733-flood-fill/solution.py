class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        change_val = image[sr][sc]
        if image[sr][sc] == color:
            return image
        queue = [(sr, sc)]
        image[sr][sc] = color
        while len(queue):
            rowIdx, colIdx = queue.pop(0)
            directions = [(-1, 0), (1,0), (0, -1), (0,1)]
            for direction in directions:
                nRowIdx = rowIdx + direction[0]
                nColIdx = colIdx + direction[1]
                if nRowIdx < 0 or nRowIdx >= len(image):
                    continue
                if nColIdx < 0 or nColIdx >= len(image[0]):
                    continue
                if image[nRowIdx][nColIdx] == change_val:
                    image[nRowIdx][nColIdx] = color
                    queue.append((nRowIdx, nColIdx))
        return image




