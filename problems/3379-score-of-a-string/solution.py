class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for idx in range(len(s) - 1):
            score += abs(ord(s[idx]) - ord(s[idx + 1]))
        return score
