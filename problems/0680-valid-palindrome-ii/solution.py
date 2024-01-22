class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        @cache
        def helper(s, l, r, allowed_errors=1):
            if l >= r:
                return True
            if s[l] == s[r]:
                return helper(s, l+1, r-1, allowed_errors)
            else:
                if allowed_errors == 0:
                    return False
                allowed_errors -= 1
                return helper(s, l+1, r, allowed_errors) or helper(s, l, r - 1, allowed_errors)
        return helper(s, 0, len(s) - 1)

