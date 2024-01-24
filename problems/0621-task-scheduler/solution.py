class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        counts = freq.values()

        t = 0
        q = []
        pq = [-c for c in counts]
        heapq.heapify(pq)

        while len(q) or len(pq):
            t += 1
            if len(pq):
                node = heapq.heappop(pq)
                node += 1
                if node < 0:
                    q.append((node, t + n))
            while len(q) and q[0][1] == t:
                node = q.pop(0)
                heapq.heappush(pq, node[0])
        return t
                



