class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"{": "}", "[": "]", "(":")"}
        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                node = stack.pop() if len(stack) else None
                if not node:
                    return False
                if mapping[node] != char:
                    return False
        return len(stack) == 0

