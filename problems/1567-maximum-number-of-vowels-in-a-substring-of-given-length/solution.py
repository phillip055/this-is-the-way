class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start, end = 0, k - 1
        x = s[start:end + 1]
        vowels = set(["a", "e", "i", "o", "u"])
        count = 0
        for char in x:
            if char in vowels:
                count += 1

        temp = count
        while end < len(s) - 1:
            end += 1
            if s[start] in vowels:
                temp -= 1
            start += 1
            if s[end] in vowels:
                temp += 1
            count = max(count, temp)
        
        return count
