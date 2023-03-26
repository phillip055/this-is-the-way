class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        def bfs(i):
            exploring = [i]
            counter = 0
            last_seen = {}
            while len(exploring):
                node = exploring.pop(0)
                if node in last_seen:
                    idx = last_seen[node]
                    return len(last_seen) - idx
                if node in visited:
                    continue
                visited.add(node)
                last_seen[node] = counter
                counter += 1
                if edges[node] == -1:
                    continue
                exploring.append(edges[node])
            return -1
        
        curr_max = -1
        for i in range(len(edges)):
            if i not in visited:
                curr_max = max(bfs(i), curr_max)
        return curr_max


