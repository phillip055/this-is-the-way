class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def outside(rowIdx, colIdx):
            return rowIdx < 0 or colIdx < 0 or rowIdx >= len(heights) or colIdx >= len(heights[0])

        def flow(rowIdx, colIdx, visited=set()):
            pacific = False
            atlantic = False
            if rowIdx == 0 or colIdx == 0:
                pacific = True
            if rowIdx == len(heights) - 1 or colIdx == len(heights[0]) - 1:
                atlantic = True
            
            if outside(rowIdx, colIdx):
                return (pacific, atlantic)
            
            directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
            for direction in directions:
                nRowIdx = rowIdx + direction[0]
                nColIdx = colIdx + direction[1]
                if not outside(nRowIdx, nColIdx) and (nRowIdx, nColIdx) not in visited:
                    if heights[rowIdx][colIdx] >= heights[nRowIdx][nColIdx]:
                        visited.add((nRowIdx, nColIdx))
                        p, a = flow(nRowIdx, nColIdx, visited)
                        pacific = pacific or p
                        atlantic = atlantic or a
            return pacific, atlantic
        result = []
        for rowIdx in range(len(heights)):
            for colIdx in range(len(heights[0])):
                res = flow(rowIdx, colIdx, set())
                if res[0] and res[1]:
                    result.append([rowIdx, colIdx])
        return result
                        




