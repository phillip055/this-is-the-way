class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        
        for l in s:
            if len(stack) > 0:
                if l == stack[-1]:
                    stack.pop()
                    continue
            stack.append(l)
        return "".join(stack)
