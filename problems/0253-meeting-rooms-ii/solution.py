class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)
        curr = 0
        intervals.sort()
        max_curr = 0
        for interval in intervals:
            if len(rooms) and interval[0] >= rooms[0]:
                curr -= 1
                heapq.heappop(rooms)
            curr += 1
            heapq.heappush(rooms, interval[1])
            max_curr = max(curr, max_curr)
        return max_curr

