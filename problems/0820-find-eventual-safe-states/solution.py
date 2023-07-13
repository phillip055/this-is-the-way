class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        order = [0] * len(graph)
        mapping = defaultdict(list)

        for idx in range(len(graph)):
            order[idx] += len(graph[idx])
            for i in graph[idx]:
                mapping[i].append(idx)

        queue = []
        for idx in range(len(order)):
            if order[idx] == 0:
                queue.append(idx)
        
        while len(queue):
            node = queue.pop(0)
            for next_node in mapping[node]:
                order[next_node] -= 1
                if order[next_node] == 0:
                    queue.append(next_node)
        
        return [i for i, x in enumerate(order) if x == 0]

