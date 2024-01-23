class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(opened, closed, stack, n):
            nonlocal result
            if closed == n:
                result.append("".join(stack))
                return
            if opened < n:
                helper(opened + 1, closed, stack + ["("], n)
            if closed < opened:
                helper(opened, closed + 1, stack + [")"], n)
        helper(0, 0 , [], n)
        return result
