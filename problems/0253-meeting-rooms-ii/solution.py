class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        heapq.heapify(rooms)

        intervals = sorted(intervals)

        max_rooms = 0
        curr = 0
        while len(intervals):
            node = intervals.pop(0)
            if len(rooms) and rooms[0] <= node[0]:
                curr -= 1
                heapq.heappop(rooms)
            curr += 1
            heapq.heappush(rooms, node[1])
            max_rooms = max(max_rooms, curr)
        return max_rooms

