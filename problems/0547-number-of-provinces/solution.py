class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        mapping = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] and i != j:
                    mapping[i].append(j)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in mapping[node]:
                dfs(n)
        
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count

