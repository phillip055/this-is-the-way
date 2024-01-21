class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.vals = []
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.vals) == self.size:
            self.sum -= self.vals.pop(0)
        self.vals.append(val)
        self.sum += val
        return self.sum / len(self.vals)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
