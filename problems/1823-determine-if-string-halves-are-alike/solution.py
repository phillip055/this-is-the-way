class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) //2
        vwls = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        return (sum(c in vwls for c in s[:mid]) ==
                        sum(c in vwls for c in s[mid:]))
            

