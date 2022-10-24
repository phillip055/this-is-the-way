class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(
            (val, min(self.getMin(), val))
        )
        return

    def pop(self) -> None:
        self.min_stack.pop()
        return

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return float('inf')
        return self.min_stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
