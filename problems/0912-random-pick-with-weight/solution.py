class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.prefix_sum = []
        for n in w:
            self.total += n
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        low, high = 0, len(self.prefix_sum) - 1
        target = random.uniform(0, self.total)
        while low <= high:
            mid = (low + high) // 2
            if self.prefix_sum[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        

        




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
