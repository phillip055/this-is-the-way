from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        mapping = defaultdict(list)
        for road in roads:
            mapping[road[0]].append(road[1:])
            mapping[road[1]].append([road[0], road[2]])
        
        exploring = [1]

        visited = set()
        result = float('inf')
        while len(exploring):
            node = exploring.pop(0)
            for next_node in mapping[node]:
                result = min(next_node[1], result)
                if next_node[0] not in visited:
                    visited.add(next_node[0])
                    exploring.append(next_node[0])
        return result

