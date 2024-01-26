class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for nodeIdx, node in enumerate(isConnected):
            for nextIdx, val in enumerate(node):
                if val:
                    adj[nodeIdx].append(nextIdx)
        
        visited = set()
        provinces = 0 
        
        def dfs(idx):
            for next_node in adj[idx]:
                if not next_node in visited:
                    visited.add(next_node)
                    dfs(next_node)
        
        for k, v in adj.items():
            if k in visited:
                continue
            else:
                provinces += 1
                visited.add(k)
                dfs(k)
        
        return provinces

