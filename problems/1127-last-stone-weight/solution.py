class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            if (diff := -1*heapq.heappop(heap) + heapq.heappop(heap)):
                heapq.heappush(heap, -diff)
        return 0 if not heap else (-1 * heap[0])

