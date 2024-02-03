class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(s, idx0, idx1, mistake=1):
            if idx0 >= idx1:
                return True
            if s[idx0] != s[idx1]:
                if mistake == 0:
                    return False
                return helper(s, idx0 + 1, idx1, mistake - 1) or helper(s, idx0, idx1-1, mistake - 1)
            return helper(s, idx0 + 1, idx1 - 1, mistake)
        
        return helper(s, 0, len(s) - 1, 1)
                
