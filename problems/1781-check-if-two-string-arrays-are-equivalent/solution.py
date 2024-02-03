class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        w1, w2 = 0, 0
        idx1, idx2 = 0, 0
        
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][idx1] != word2[w2][idx2]:
                return False
            
            idx1 += 1
            idx2 += 1
            
            if idx1 == len(word1[w1]):
                w1 += 1
                idx1 = 0
            
            if idx2 == len(word2[w2]):
                w2 += 1
                idx2 = 0
            
        return w1 == len(word1) and w2 == len(word2)
        
