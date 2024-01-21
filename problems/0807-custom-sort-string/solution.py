class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = [cnt.pop(c, 0) * c for c in order]
        for c, v in cnt.items():
            ans.append(c * v)
        return ''.join(ans)

