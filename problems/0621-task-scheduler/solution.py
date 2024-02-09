class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        interval = 0
        
        freq = Counter(tasks)
        
        q = []
        
        pq = [(-v, k) for k, v in freq.items()]
        
        heapq.heapify(pq)
        
        while len(pq) or len(q):
            interval += 1
            
            if len(pq):
                item = heapq.heappop(pq)
                if item[0] + 1 < 0:
                    q.append((item[0] + 1, item[1], interval + n))
            
            while len(q) and q[0][2] <= interval:
                item = q.pop(0)
                heapq.heappush(pq, (item[0], item[1]))
        return interval
                
        
        
