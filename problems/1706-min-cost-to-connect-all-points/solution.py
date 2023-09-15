class Solution:

    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = []
        costs = defaultdict(list)
        n = len(points)

        for idx0 in range(n):
            for idx1 in range(n):
                if idx0 == idx1:
                    continue
                xi, yi = points[idx0]
                xj, yj = points[idx1]
                dist = abs(xi-xj) + abs(yi-yj)
                costs[xi,yi].append((dist, xj,yj))
        
        min_cost = 0
        x0, y0 = points[0]
        heappush(heap, (0, x0, y0))
        while heap:
            dist, x, y = heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x,y))
            min_cost += dist
            for next_point in costs[x,y]:
                _, x, y = next_point
                heappush(heap, next_point)
        return min_cost

            

