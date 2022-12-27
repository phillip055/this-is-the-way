class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainingCapacity = [x - y for (x, y) in zip(capacity, rocks)]
        remainingCapacity = sorted(remainingCapacity)

        fullBagsCount = 0
        for c in remainingCapacity:
            if c == 0:
                fullBagsCount += 1
            elif c <= additionalRocks:
                additionalRocks -= c
                fullBagsCount += 1
        return fullBagsCount
