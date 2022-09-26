class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            if current_interval[1] >= intervals[i][0]:
                current_interval[1] = max(intervals[i][1], current_interval[1])
            else:
                res.append(current_interval)
                current_interval = intervals[i]
        res.append(current_interval)
        return res
            
