class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        safe = {}
        def dfs(idx):
            if idx in safe:
                return safe[idx]
            safe[idx] = False
            for next_node in graph[idx]:
                if not dfs(next_node):
                    return safe[idx]
            safe[idx] = True
            return safe[idx]

        result = []
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result

