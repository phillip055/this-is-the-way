class Solution:
    def topKFrequent(self, nums: List[int], cap: int) -> List[int]:
        freq = Counter(nums)
        pq = []
        heapq.heapify(pq)
        for k,v in freq.items():
            heapq.heappush(pq, (v, k))
            if len(pq) > cap:
                heapq.heappop(pq)
        
        return [x[1] for x in pq]

