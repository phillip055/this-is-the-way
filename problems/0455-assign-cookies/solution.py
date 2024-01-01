class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        result, i, j, = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                i += 1
        return result

