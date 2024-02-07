class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [None] * len(graph)

        for edge in range(len(graph)):
            if colors[edge] == None:
                colors[edge] = 1
                to_explore = deque([edge])
                while len(to_explore):
                    node = to_explore.popleft()
                    for _next in graph[node]:
                        if not colors[_next]:
                            colors[_next] = 1 - colors[node]
                            to_explore.append(_next)
                        elif colors[node] == colors[_next]:
                            return False
        return True

