class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=set()
        
        toFlip = set()
        
        def getNeighbors(i,j):
            ns = []
            if i - 1 >= 0:
                ns.append((i-1, j))
            if i + 1 < len(board):
                ns.append((i+1, j))
            if j - 1 >= 0:
                ns.append((i, j-1))
            if j + 1 < len(board[0]):
                ns.append((i, j+1))
            return ns
        
        def explore(i,j):
            group = []
            
            toExplore = [(i,j)]
            
            while toExplore:
                node = toExplore.pop(0)
                ns = getNeighbors(node[0], node[1])
                group.append(node)
                visited.add(node)
                for n in ns:
                    if n in visited:
                        continue
                    if board[n[0]][n[1]] == "O":
                        if n not in toExplore:
                            toExplore.append(n)
            
            surrounded = True
            for g in group:
                if g[0] == 0 or g[0] == len(board) - 1 or g[1] == 0 or g[1] == len(board[0]) - 1:
                    surrounded = False
            if surrounded:
                for g in group:
                    toFlip.add(g)
            return;
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if (i,j) in visited:
                        continue
                    explore(i,j)
        
        for f in toFlip:
            board[f[0]][f[1]] = "X"
