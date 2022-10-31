class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def getNeighbors(board, i ,j):
            n = []
            if i - 1 >= 0:
                n.append((i-1, j))
            if i + 1 <= len(board) - 1:
                n.append((i+1, j))
            if j - 1 >= 0:
                n.append((i, j-1))
            if j + 1 <= len(board[0]) - 1:
                n.append((i, j+1))
            if i - 1 >= 0 and j - 1 >= 0:
                n.append((i-1, j-1))
            if i + 1 <= len(board) -1 and j - 1 >= 0:
                n.append((i+1, j-1))
            if i - 1 >= 0 and j + 1 <= len(board[0]) - 1:
                n.append((i-1, j+1))
            if i + 1 <= len(board) - 1 and j + 1 <= len(board[0]) - 1:
                n.append((i+1, j+1))
            return n
            
        new = set()
        remove = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                print("From: " + str(i) + "," + str(j))
                val = board[i][j]
                print(val)
                ns = getNeighbors(board, i,j)
                print(ns)
                notice = list(map(lambda x: "alive" if board[x[0]][x[1]] else "dead", ns))
                aliveNs = list(filter(lambda x: x == "alive", notice))
                print(aliveNs)
                deadNs = list(filter(lambda x: x == "dead", notice))
                print(deadNs)
                if val == 1:
                    if len(aliveNs) < 2:
                        print("Kill Him")
                        remove.add((i,j))
                        continue
                    if len(aliveNs) == 2 or len(aliveNs) == 3:
                        print("Let Him Live")
                        continue
                    if len(aliveNs) > 3:
                        print("Kill Him")
                        remove.add((i,j))
                        continue
                else:
                    if len(aliveNs) == 3:
                        print("Get him alive")
                        new.add((i,j))
                        continue
        
        for n in new:
            board[n[0]][n[1]] = "1"
        for r in remove:
            board[r[0]][r[1]] = "0"
