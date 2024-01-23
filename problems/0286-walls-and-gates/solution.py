class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        to_explore = []
        for rowIdx in range(len(rooms)):
            for colIdx in range(len(rooms[0])):
                if rooms[rowIdx][colIdx] == 0:
                    to_explore.append((rowIdx, colIdx, 0))

        def outside(rowIdx, colIdx):
            return rowIdx < 0 or rowIdx >= len(rooms) or colIdx < 0 or colIdx >= len(rooms[0])

        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        while len(to_explore):
            rowIdx, colIdx, distance = to_explore.pop(0)
            for direction in directions:
                nRowIdx = rowIdx + direction[0]
                nColIdx = colIdx + direction[1]
                if not outside(nRowIdx, nColIdx) and rooms[nRowIdx][nColIdx] == 2147483647:
                    rooms[nRowIdx][nColIdx] = distance + 1
                    to_explore.append((nRowIdx, nColIdx, distance + 1))


