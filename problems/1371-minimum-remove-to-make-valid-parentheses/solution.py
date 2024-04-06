class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if not len(stack):
                    to_remove.add(idx)
                else:
                    stack.pop()
        for e in stack:
            to_remove.add(e)
        
        result = []
        for idx, char in enumerate(s):
            if idx in to_remove:
                continue
            result.append(char)
        return "".join(result)

