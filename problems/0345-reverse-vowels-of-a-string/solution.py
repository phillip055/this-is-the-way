class Solution:
    def reverseVowels(self, s: str) -> str:
        idx0, idx1 = 0, len(s) - 1
        def is_vowel(ch):
            return ch in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        s = list(s)
        while idx0 < idx1:
            print(idx0, idx1)
            if is_vowel(s[idx0]) and is_vowel(s[idx1]):
                s[idx0], s[idx1] = s[idx1], s[idx0]
                idx0 += 1
                idx1 -= 1
            elif is_vowel(s[idx0]):
                idx1 -= 1
            elif is_vowel(s[idx1]):
                idx0 += 1
            else:
                idx0 += 1
                idx1 -= 1
        return "".join(s)
    
