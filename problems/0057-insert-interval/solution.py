class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        position = bisect.bisect_left(intervals, newInterval) 
        intervals.insert(position, newInterval)

        def mergeIntervals(intervals):
            if not len(intervals):
                return []
            result = [intervals[0]]
            for intervalIdx in range(1, len(intervals)):
                interval = intervals[intervalIdx]
                if interval[0] <= result[-1][1]:
                    result[-1][1] = max(interval[1], result[-1][1])
                else:
                    result.append(interval)
            return result
        
        return mergeIntervals(intervals)

