class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in l:
                if i & j:
                    continue
                l.append(i | j)
        m = 0
        for i in l:
            if m < len(i):
                m = len(i)
        return m
