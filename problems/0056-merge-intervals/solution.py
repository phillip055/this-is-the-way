class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        print(intervals)
        for idx in range(len(intervals)):
            interval = intervals[idx]
            if result == []:
                result.append(interval)
            else:
                prevInterval = result[-1]
                if prevInterval[1] >= interval[0] and prevInterval[1] < interval[1]:
                    result[-1][1] = interval[1]
                else:
                    if prevInterval[0] <= interval[0] and prevInterval[1] >= interval[1]:
                        continue
                    if prevInterval == interval:
                        continue
                    result.append(interval)
        return result
            
