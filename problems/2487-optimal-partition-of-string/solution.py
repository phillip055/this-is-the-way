class Solution:
    def partitionString(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lookup = set()
        ans = 1
        for char in s:
            if char in lookup:
                ans += 1
                lookup = set()
            lookup.add(char)
        return ans

