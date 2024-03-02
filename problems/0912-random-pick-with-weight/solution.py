class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.prefix_sums = []
        for e in w:
            self.total += e
            self.prefix_sums.append(self.total)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.total)
        low, high = 0, len(self.prefix_sums) - 1
        idx = bisect.bisect(self.prefix_sums, target)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
