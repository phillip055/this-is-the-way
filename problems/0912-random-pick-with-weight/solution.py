class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [0]
        self.total = 0
        for num in w:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
            self.total += num
        self.prefix_sum.pop(0)

    def pickIndex(self) -> int:
        v = random.uniform(0, self.total)
        l, r = 0, len(self.prefix_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.prefix_sum[mid] >= v:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
