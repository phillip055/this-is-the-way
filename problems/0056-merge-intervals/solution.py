class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not len(intervals):
            return []
        intervals.sort()
        result = []
        prev = intervals[0]
        for idx in range(1, len(intervals)):
            curr = intervals[idx]
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(prev)
                prev = curr
        result.append(prev)
        return result
