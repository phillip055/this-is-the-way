class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def explore(i,j):
            toExplore = [(i,j)]
            while toExplore:
                node = toExplore.pop(0)
                if node in visited:
                    continue
                if grid[node[0]][node[1]] == "0":
                    continue
                visited.add(node)
                toExplore += getNeigbors(node[0], node[1])
            return;
        
        def getNeigbors(i,j):
            neigbors = []
            if i+1 <= len(grid) - 1:
                neigbors.append((i + 1, j))
            if i-1 >= 0:
                neigbors.append((i - 1, j))
            if j-1 >= 0:
                neigbors.append((i, j - 1))
            if j+1 <= len(grid[0]) - 1:
                neigbors.append((i, j + 1))
            return neigbors
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited or grid[i][j] == "0":
                    continue
                explore(i,j)
                islands += 1
        return islands

