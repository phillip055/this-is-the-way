class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        keys.add(0)

        visitedRooms = set()

        while keys:
            key = keys.pop()
            if key in visitedRooms:
                continue
            visitedRooms.add(key)
            unlockedKeys = rooms[key]
            for k in unlockedKeys:
                if k in visitedRooms:
                    continue
                keys.add(k)
            
        return len(visitedRooms) == len(rooms)

