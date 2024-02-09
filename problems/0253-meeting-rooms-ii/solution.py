class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        rooms = []
        heapq.heapify(rooms)
        
        max_concurrent_room = 0
        rooms_required_atm = 0
        for interval in intervals:
            rooms_required_atm += 1
            if len(rooms) and rooms[0] <= interval[0]:
                heapq.heappop(rooms)
                rooms_required_atm -= 1
            heapq.heappush(rooms, interval[1])
            max_concurrent_room = max(rooms_required_atm, max_concurrent_room)
        return max_concurrent_room

