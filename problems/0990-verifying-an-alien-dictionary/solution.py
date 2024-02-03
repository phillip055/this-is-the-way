class Solution:
    def isAlienSorted(self, words: List[str], o: str) -> bool:
        order = {}
        for idx, char in enumerate(o):
            order[char] = idx
        def lessThan(w1, w2):
            idx0, idx1 = 0, 0
            while idx0 < len(w1) and idx1 < len(w2):
                if order[w1[idx0]] > order[w2[idx1]]:
                    return False
                if order[w1[idx0]] < order[w2[idx1]]:
                    return True
                idx0 += 1
                idx1 += 1
            return len(w1) <= len(w2)
        
        for idx in range(1, len(words)):
            prev_word, word = words[idx-1], words[idx]
            if not lessThan(prev_word, word):
                return False
        return True
                
        
