class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            diff = heappop(heap) - heappop(heap)
            heappush(heap, diff)
        return heap[0] * -1
