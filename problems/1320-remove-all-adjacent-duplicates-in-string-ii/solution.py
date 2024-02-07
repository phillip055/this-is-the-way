class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        stack = []
        for char in s:
            if not len(stack) or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                prev = stack.pop()
                if prev[1] + 1 == k:
                    continue
                else:
                    stack.append((prev[0], prev[1] + 1))
        result = ""
        for e in stack:
            result += e[0] * e[1]
        return result

