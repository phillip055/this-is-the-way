class Solution:
    def minInsertions(self, s: str) -> int:

        @cache
        def rec(l, r):
            if l > r:
                return 0
            if s[l] == s[r]:
                return rec(l+1, r-1)
            else:
                return 1 + min(rec(l+1, r), rec(l, r-1))
        
        return rec(0, len(s)-1)

