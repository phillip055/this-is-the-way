class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append((idx, ch))
            if ch == ")":
                if len(stack):
                    stack.pop()
                else:
                    to_remove.add(idx)
        for e in stack:
            to_remove.add(e[0])
        
        result = []
        for idx, ch in enumerate(s):
            if idx in to_remove:
                continue
            else:
                result.append(ch)
        return "".join(result)

