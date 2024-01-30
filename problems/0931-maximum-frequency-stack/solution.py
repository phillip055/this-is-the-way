class FreqStack:

    def __init__(self):
        self.q = []
        self.freq = defaultdict(int)
        self.pos = 0

    def push(self, val: int) -> None:
        heapq.heappush(self.q, (-self.freq[val], -self.pos, val))
        self.freq[val] += 1
        self.pos += 1

    def pop(self) -> int:
        x = heapq.heappop(self.q)[2]
        self.freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
