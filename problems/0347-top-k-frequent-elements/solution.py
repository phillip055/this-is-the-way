class Solution:
    def topKFrequent(self, nums: List[int], capacity: int) -> List[int]:
        freq = Counter(nums)
        result = []
        heapq.heapify(result)
        for k, v in freq.items():
            heapq.heappush(result, (v, k))
            if len(result) > capacity:
                heapq.heappop(result)
        return [e[1] for e in result]

