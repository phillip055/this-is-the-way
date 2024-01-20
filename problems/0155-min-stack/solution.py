class MinStack:

    def __init__(self):
        self.min_history = []
        self.vals = []

    def push(self, val: int) -> None:
        if len(self.min_history):
            self.min_history.append(min(self.min_history[-1], val))
        else:
            self.min_history.append(val)
        self.vals.append(val)
    def pop(self) -> None:
        self.vals.pop()
        self.min_history.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min_history[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
