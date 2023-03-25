from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for edge in edges:
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])
        
        visited = set()

        def bfs(i):
            exploring = [i]
            size = 0
            while len(exploring):
                node = exploring.pop(0)
                if node in visited:
                    continue
                size += 1
                visited.add(node)
                for x in mapping[node]:
                    if x not in visited:
                        exploring.append(x)
            return size
        
        cluster_sizes = []
        for x in range(n):
            if x not in visited:
                res = bfs(x)
                cluster_sizes.append(res)

        if len(cluster_sizes) <= 1:
            return 0
        result = 0
        acc = cluster_sizes[0]
        for i in range(1, len(cluster_sizes)):
            result += acc * cluster_sizes[i]
            acc += cluster_sizes[i] 
        return result

