class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        overlap_len = min(len(word1), len(word2))
        for idx in range(overlap_len):
            result += word1[idx]
            result += word2[idx]
        for idx in range(overlap_len, len(word1)):
            result += word1[idx]
        for idx in range(overlap_len, len(word2)):
            result += word2[idx]
        return result

