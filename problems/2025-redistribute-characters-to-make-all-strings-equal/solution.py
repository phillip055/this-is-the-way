class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = Counter()
        for word in words:
            counter.update(word)
        
        for letter, count in counter.items():
            if count % len(words) != 0:
                return False
        return True

