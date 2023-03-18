class BrowserHistory:
    def __init__(self, homepage: str):
        self.historyStack = []
        self.forwardStack = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.historyStack.append(self.current)
        self.current = url
        self.forwardStack = []
        print(self.current, self.historyStack, self.forwardStack)

    def back(self, steps: int) -> str:
        for i in range(min(steps, len(self.historyStack))):
            self.forwardStack.insert(0, self.current)
            self.current = self.historyStack.pop()
        return self.current

    def forward(self, steps: int) -> str:
        for i in range(min(steps, len(self.forwardStack))):
            self.historyStack.append(self.current)
            self.current = self.forwardStack.pop(0)
        return self.current

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
