class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, start, end, allowed_mistake=1):
            if end <= start:
                return True
            if s[start] == s[end]:
                return helper(s, start + 1, end - 1, allowed_mistake)
            else:
                if allowed_mistake == 0:
                    return False
                else:
                    return helper(s, start + 1, end, allowed_mistake-1) or helper(s, start, end - 1, allowed_mistake-1)
            
        return helper(s, 0, len(s)-1)
