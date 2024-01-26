class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.result = deque([])
        self.total_sum = 0

    def next(self, val: int) -> float:
        self.result.append(val)
        self.total_sum += val
        while len(self.result) > self.size:
            node = self.result.popleft()
            self.total_sum -= node
        return self.total_sum / len(self.result)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
