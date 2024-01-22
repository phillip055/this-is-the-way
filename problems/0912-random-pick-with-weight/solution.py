class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        pick = random.uniform(0, self.total)

        l, r = 0, len(self.prefix_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] < pick:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
