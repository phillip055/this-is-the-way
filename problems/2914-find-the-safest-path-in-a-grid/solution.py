class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        multi_source_queue = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    multi_source_queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        while multi_source_queue:
            size = len(multi_source_queue)
            while size > 0:
                curr = multi_source_queue.popleft()
                for d in self.directions:
                    di, dj = curr[0] + d[0], curr[1] + d[1]
                    val = grid[curr[0]][curr[1]]
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        multi_source_queue.append((di, dj))
                size -= 1
        
        pq = [[-grid[0][0], 0, 0]]
        grid[0][0] = -1

        while pq:
            safeness, i, j = heapq.heappop(pq)
            if i == n - 1 and j == n - 1:
                return -safeness
            
            for d in self.directions:
                di, dj = i + d[0], j + d[1]
                if self.isValidCell(grid, di, dj) and grid[di][dj] != -1:
                    heapq.heappush(pq, [-min(-safeness, grid[di][dj]), di, dj])
                    grid[di][dj] = -1

        return -1
    
    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

