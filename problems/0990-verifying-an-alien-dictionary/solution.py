class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash = {}
        for i, e in enumerate(order):
            hash[e] = i

        def lessThan(w1, w2):
            for e1, e2 in zip(w1, w2):
                if e1 == e2:
                    continue
                return hash[e1] < hash[e2]
            return len(w1) <= len(w2)
        
        for idx in range(1, len(words)):
            if not lessThan(words[idx - 1], words[idx]):
                return False
        
        return True
        
