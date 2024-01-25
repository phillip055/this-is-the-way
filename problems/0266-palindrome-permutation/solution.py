class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(s)
        odds = list(filter(lambda f: f % 2 != 0, freq.values()))
        return len(odds) <= 1

