class Solution:
    def topKFrequent(self, nums: List[int], capacity: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        heapq.heapify(heap)
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > capacity:
                heapq.heappop(heap)
        return [element[1] for element in heap]

