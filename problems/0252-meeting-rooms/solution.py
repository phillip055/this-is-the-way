class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals = sorted(intervals)
        
        current_meeting = intervals[0]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < current_meeting[1]:
                return False
            current_meeting[1] = max(intervals[idx][1], current_meeting[1])
        return True

