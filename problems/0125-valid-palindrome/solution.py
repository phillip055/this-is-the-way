class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda x: x.isalpha() or x.isdigit(), list(s)))
        idx0, idx1 = 0, len(s) - 1
        while idx0 < idx1:
            if s[idx0].lower() != s[idx1].lower():
                return False
            idx0 += 1
            idx1 -= 1
        return True

