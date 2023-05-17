class Solution:
    def reverseWords(self, s: str) -> str:
        letters = ""

        for c in s:
            if len(letters) and letters[-1] == " " and c == " ":
                continue
            else:
                letters += c
        
        letters = letters.strip()
        return " ".join(list(reversed(letters.split(" "))))

