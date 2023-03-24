from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for conn in connections:
            # Map with fakes
            mapping[conn[0]].append((conn[1], False))
            mapping[conn[1]].append((conn[0], True))

        result = 0
        exploring = [0]
        visited = set()
        while(exploring):
            node = exploring.pop()
            visited.add(node)
            for next_node, fake in mapping[node]:
                if next_node not in visited:
                    exploring.append(next_node)
                    if not fake: result+=1
        return result

