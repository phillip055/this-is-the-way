class Solution:
    def isPalindrome(self, s: str) -> bool:
        idx0, idx1 = 0, len(s) - 1
        while idx0 < idx1:
            c0 = s[idx0].lower()
            c1 = s[idx1].lower()
            if not c0.isnumeric() and not c0.isalpha() or c0 == " ":
                idx0 += 1
                continue
            if not c1.isnumeric() and not c1.isalpha() or c1 == " ":
                idx1 -= 1
                continue
            if c0 != c1:
                return False
            idx0 += 1
            idx1 -= 1
        return True

