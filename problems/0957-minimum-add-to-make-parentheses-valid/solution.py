class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        adds = 0
        for char in s:
            if char == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    adds += 1
                else:
                    stack.pop()
        return adds + len(stack)
        
