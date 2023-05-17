class Solution:
    def reverseVowels(self, s: str) -> str:
        idx0, idx1 = 0, len(s) - 1
        s = list(s)
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        while idx0 < idx1:
            if s[idx1] in vowels and s[idx0] in vowels:
                s[idx0], s[idx1] = s[idx1], s[idx0]
                idx0 += 1
                idx1 -= 1

            if s[idx0] not in vowels:
                idx0 += 1
            if s[idx1] not in vowels:
                idx1 -= 1

        return "".join(s)
        
