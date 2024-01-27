class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        idx0, idx1 = 0, len(s) - 1
        s = list(s)
        while idx0 < idx1:
            if not s[idx0].isalpha() or s[idx0].isnumeric():
                idx0 += 1
            elif not s[idx1].isalpha() or s[idx1].isnumeric():
                idx1 -= 1
            else:
                s[idx0], s[idx1] = s[idx1], s[idx0]
                idx0 += 1
                idx1 -= 1
        return "".join(s)
            
