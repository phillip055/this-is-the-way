class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        t = max(time)
        l, r = 1, t*totalTrips

        while l < r:
            mid = (l+r) // 2
            cost = 0
            for i in range(len(time)):
                cost += mid//time[i]
            if cost >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l


