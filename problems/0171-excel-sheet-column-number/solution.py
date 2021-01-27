class Solution:
    def titleToNumber(self, s: str) -> int:
        return ord(s)-64 if len(s)==1 else self.titleToNumber(s[1:])+(ord(s[0])-64)*26**(len(s)-1)
