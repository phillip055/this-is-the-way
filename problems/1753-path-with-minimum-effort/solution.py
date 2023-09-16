class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap, visited = [], set()
        n, m = len(heights), len(heights[0])

        heappush(heap, (0, 0, 0))
        max_diff = 0

        while heap:
            _max_diff, i, j = heappop(heap)
            if (i,j) in visited:
                continue
            max_diff = max(max_diff, _max_diff)
            if i == n - 1 and j == m - 1:
                return max_diff
            visited.add((i,j))
            for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
                next_x, next_y = i + dx, j + dy
                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                    continue
                heappush(
                    heap, (
                        abs(heights[i][j] - heights[next_x][next_y]),
                        next_x,
                        next_y
                    )
                )
        return max_diff
            
    
            

