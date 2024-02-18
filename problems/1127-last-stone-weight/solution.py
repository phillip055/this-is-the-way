class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap):
            node1 = heapq.heappop(heap)
            if len(heap) == 0:
                return -1 * node1
            node2 = heapq.heappop(heap)
            result = node1 - node2
            if result != 0:
                heapq.heappush(heap, result)
        return 0

