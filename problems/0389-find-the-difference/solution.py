class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = set(t) - set(s)
        if len(diff):
            return list(diff)[0] 
        s = dict(Counter(s))
        t = dict(Counter(t))
        for x in s:
            if s[x] != t[x]:
                return x

