class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        adds = 0
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    adds += 1
        return adds + len(stack)    

