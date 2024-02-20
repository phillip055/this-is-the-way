class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        pq = [-v for k, v in freq.items()]
        heapq.heapify(pq)
        q = []
        
        time = 0
        
        while len(pq) or len(q):
            time += 1
            if len(pq):
                remaining = heapq.heappop(pq)
                if remaining + 1 < 0:
                    q.append((remaining + 1, time + n))
            while len(q) and q[0][1] <= time:
                node = q.pop(0)
                heapq.heappush(pq, node[0])
        return time
            
        
