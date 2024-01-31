class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_weight = {}
        for idx, char in enumerate(order):
            char_weight[char] = idx
        
        def lesserThan(word1, word2):
            idx = 0 
            while idx < len(word1) and idx < len(word2):
                if char_weight[word1[idx]] == char_weight[word2[idx]]:
                    idx += 1
                elif char_weight[word1[idx]] > char_weight[word2[idx]]:
                    return False
                else:
                    return True
            return len(word1) <= len(word2)
        
        for idx in range(1, len(words)):
            if not lesserThan(words[idx-1], words[idx]):
                return False
        return True
            
        
