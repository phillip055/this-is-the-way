class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def generator(words):
            for word in words:
                for c in word:
                    yield c
            yield None
        for i, j in zip(generator(word1), generator(word2)):
            if i != j:
                return False
        return True
        

