class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        adds = 0
        for x in s:
            if x == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    adds += 1
                else:
                    d = stack.pop()
        return adds + len(stack)

