class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # To use less space, put the shortest string first
        if len(text1) > len(text2):
            text1, text2 = text2, text1
        prev = [0] * (len(text1) + 1)
        next = [0] * (len(text1) + 1)
        for i2 in range(len(text2)):
            for i1 in range(len(text1)):
                next[i1 + 1] = max(next[i1], prev[i1 + 1], prev[i1] + (text1[i1] == text2[i2]))
            prev, next = next, prev
        return prev[-1]


            
