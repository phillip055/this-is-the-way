class Solution:
    def topKFrequent(self, nums: List[int], cap: int) -> List[int]:
        freq = Counter(nums)
        result = []
        heapq.heapify(result)
        for k,v in freq.items():
            heapq.heappush(result, (v, k))
            if len(result) > cap:
                heapq.heappop(result)
        return [x[1] for x in result]
