class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        one = Counter(word1)
        two = Counter(word2)
        
        if sorted(one.keys()) == sorted(two.keys()) and sorted(one.values()) == sorted(two.values()):
            return True
        return False
