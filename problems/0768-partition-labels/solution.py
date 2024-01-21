class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def mergeIntervals(intervals):
            intervals = sorted(intervals, key=lambda x: x[0])
            merged_intervals = []
            current_interval = intervals[0]
            for idx in range(1, len(intervals)):
                new_interval = intervals[idx]
                if new_interval[0] < current_interval[1]:
                    current_interval[1] = max(new_interval[1], current_interval[1])
                else:
                    merged_intervals.append(current_interval)
                    current_interval = new_interval
            merged_intervals.append(current_interval)
            return merged_intervals
        intervals = {}
        for idx, char in enumerate(s):
            if char in intervals:
                intervals[char] = [intervals[char][0], idx]
            else:
                intervals[char] = [idx, idx]
        merged = mergeIntervals(intervals.values())
        return list(map(lambda x: x[1] - x[0] + 1, merged))

        
        


