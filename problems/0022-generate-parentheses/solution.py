class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(n, opened=0, closed=0, stack=[]):
            if closed == n:
                result.append("".join(stack))
                return
            if opened < n:
                helper(n, opened + 1, closed, stack + ["("])
            if closed < opened:
                helper(n, opened, closed + 1, stack + [")"])
        helper(n)
        return result

