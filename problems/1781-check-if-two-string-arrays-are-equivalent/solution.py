class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        for word in word1:
            w1 += word
        w2 = ""
        for word in word2:
            w2 += word
        return w1 == w2
