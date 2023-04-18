class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for a, b in zip(word1, word2):
            result += a
            result += b
        remainingIdx = min(len(word1), len(word2))
        return result + word1[remainingIdx:] + word2[remainingIdx:]

