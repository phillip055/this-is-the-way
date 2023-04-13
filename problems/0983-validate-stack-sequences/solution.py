class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and idx < len(popped) and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1

        return idx == len(popped)

