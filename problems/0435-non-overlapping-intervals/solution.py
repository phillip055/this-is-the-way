class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        current = intervals[0]
        count = 0
        for idx in range(1, len(intervals)):
            if current[1] > intervals[idx][0]:
                count += 1
                current[0], current[1] = min(intervals[idx][0], current[0]), min(intervals[idx][1], current[1])
            else:
                current = intervals[idx]
        return count

