# firstList = intervals
# secondList = [newInterval]

# [[1,3], [2,5], [6,9]]
# 
# [1,5]



# [1,10]
# [2,5]

# [3,10]
# [2,5]
# [2,10]

# Algorithm
# mergable = check if newInterval[0] <= interval[1]
# to_insert_interval = (min(newInterval[0], min(interval[0]), max(newInteraval[1], interval[1])))

# O(n), O(n)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                output.append(newInterval)
                return output + intervals[idx:]
            elif newInterval[0] > intervals[idx][1]:
                output.append(intervals[idx])
            else:
                newInterval = [
                    min(newInterval[0], intervals[idx][0]),
                    max(newInterval[1], intervals[idx][1])
                ]
        output.append(newInterval)
        return output

