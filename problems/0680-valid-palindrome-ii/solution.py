class Solution:
    def validPalindrome(self, s: str) -> bool:
        @cache
        def helper(s, left, right, incorrectAllowed):
            if left > right:
                return True
            if incorrectAllowed == -1:
                return False
            if s[left] == s[right]:
                return helper(s, left + 1, right - 1, incorrectAllowed)
            return helper(s, left + 1, right, incorrectAllowed - 1) or helper(s, left, right - 1, incorrectAllowed - 1)
        
        return helper(s, 0, len(s) - 1, 1)

