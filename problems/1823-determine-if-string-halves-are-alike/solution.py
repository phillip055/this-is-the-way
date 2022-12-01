class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) //2
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        firstHalfCount = 0
        for i in range(mid):
            if s[i] in vowels:
                firstHalfCount += 1
        
        for i in range(mid, len(s)):
            if s[i] in vowels:
                firstHalfCount -= 1
        return firstHalfCount == 0
