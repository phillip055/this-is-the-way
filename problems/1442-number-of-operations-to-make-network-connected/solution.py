from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        mapping = defaultdict(list)
        for conn in connections:
            mapping[conn[0]].append(conn[1])
            mapping[conn[1]].append(conn[0])
        
        visited = set()
        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            for x in mapping[i]:
                dfs(x)
            return 1

        # number of server cluster - 1 = number of connections required to connect all matchines
        return sum(dfs(i) for i in range(n)) - 1

