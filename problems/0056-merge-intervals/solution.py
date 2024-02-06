class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not len(intervals):
            return []
        intervals.sort()
        result = [intervals[0]]
        for idx in range(1, len(intervals)):
            node = intervals[idx]
            prev = result[-1]
            if node[0] > prev[1]:
                result.append(node)
            else:
                prev[1] = max(node[1], prev[1])
        return result
