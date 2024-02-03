class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        idx0, idx1 = 0, len(s) - 1
        
        while idx0 < idx1:
            if not s[idx0].isnumeric() and not s[idx0].isalpha():
                idx0 += 1
                continue
            if not s[idx1].isnumeric() and not s[idx1].isalpha():
                idx1 -= 1
                continue
            if s[idx0].lower() != s[idx1].lower():
                return False
            idx0 += 1
            idx1 -= 1
        return True
        
