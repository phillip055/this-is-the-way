class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        routes = defaultdict(list)
        for edge in edges:
            routes[edge[0]].append(edge[1]) 
            routes[edge[1]].append(edge[0]) 

        visited = set()
        explore = deque([source])

        while explore:
            node = explore.popleft()
            if node in visited:
                continue
            visited.add(node)
            if node == destination:
                return True
            if node in routes:
                for r in routes[node]:
                    if r not in visited:
                        explore.append(r)
            
        return False
            
            
