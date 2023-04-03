class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        idx0, idx1 = 0, len(people) - 1
        boats = 0
        while idx0 <= idx1:
            boats += 1
            if people[idx0] + people[idx1] <= limit:
                idx0 += 1
            idx1 -= 1
        return boats        

