class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def getNeighbors(board, i, j):
            n = []
            if i + 1 <= len(board) - 1:
                n.append((i+1, j))
            if i - 1 >= 0:
                n.append((i-1, j))
            if j + 1 <= len(board[0]) - 1:
                n.append((i, j+1))
            if j - 1 >= 0:
                n.append((i, j-1))
            return n
        
        def dfs(word, board, i, j, visited=set()):
            if (i,j) in visited:
                return False
            if word == "":
                return True
            visited.add((i,j))
            n = getNeighbors(board, i,j)
            for e in n:
                if board[e[0]][e[1]] == word[0] and dfs(word[1:], board, e[0], e[1], visited):
                    return True
            visited.remove((i,j))
            return False
                
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(word[1:], board, i, j):
                    return True
        return False
                    
