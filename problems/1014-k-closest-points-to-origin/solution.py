class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dots = []
        for x, y in points:
            dots.append([x ** 2 + y ** 2, x, y])

        heapq.heapify(dots)
        result = []
        while k > 0:
            k-=1
            _, x, y = heapq.heappop(dots)
            result.append([x, y])
        return result
