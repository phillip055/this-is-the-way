class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def timeRequired(dist: List[int], speed: float) -> int:
            time = 0
            for _dist in dist[:-1]:
                time += math.ceil(_dist/speed)
            time += dist[-1]/speed
            return time
        
        left, right = 1, 1e7
        minSpeed = -1

        while left <= right:
            mid = (left + right) // 2
            if timeRequired(dist, mid) <= hour:
                minSpeed = mid
                right = mid - 1
            else:
                left = mid + 1
        return int(minSpeed) if (math.ceil(minSpeed) == math.floor(minSpeed)) else mindSpeed

