class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> None:
        self.array.pop()
        

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return min(self.array)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
