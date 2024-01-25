class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""]*len(words)

        for word in words:
            word = list(word)
            idx = word.pop()
            result[int(idx) - 1] = "".join(word)
        return " ".join(result)

