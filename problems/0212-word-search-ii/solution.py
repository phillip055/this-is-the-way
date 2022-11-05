class Trie:
    table = {}
    def __init__(self):
        self.table = {}
        return
    
    def addWord(self, word):
        t = self.table
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["*"] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def getNeighbors(board, i, j):
            ns = []
            if i + 1 <= len(board) - 1:
                ns.append((i+1,j))
            if i - 1 >= 0:
                ns.append((i-1, j))
            if j + 1 <= len(board[0]) - 1:
                ns.append((i,j+1))
            if j - 1 >= 0:
                ns.append((i, j-1))
            return ns
        
        
        trie = Trie()
        notFound = set(words)
        visited = set()

        for word in words:
            trie.addWord(word)
        
        def dfs(board, i, j, trie, visited, notFound):
            if (i,j) in visited:
                return False
            if "*" in trie:
                if trie["*"] in notFound:
                    notFound.remove(trie["*"])
            if trie == {}:
                return 
            visited.add((i,j))
            ns = getNeighbors(board, i, j)
            for n in ns:
                if board[n[0]][n[1]] in trie:
                    dfs(board, n[0], n[1], trie[board[n[0]][n[1]]], visited, notFound)
            visited.remove((i,j))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.table:
                    dfs(board, i, j, trie.table[board[i][j]], visited, notFound)
                trie = Trie()
                for word in notFound:
                    trie.addWord(word)
        return set(words) - notFound
                    
