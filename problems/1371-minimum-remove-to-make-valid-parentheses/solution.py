class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append((ch, idx))
            if ch == ")":
                if len(stack):
                    stack.pop()
                else:
                    to_remove.add(idx)
        for (opening_bracket, idx) in stack:
            to_remove.add(idx)

        result = []
        for idx, ch in enumerate(s):
            if idx in to_remove:
                continue
            else:
                result.append(ch)
        return "".join(result)
        
