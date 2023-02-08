class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pairs = sorted(Counter(words).items(), key = lambda p: (-p[1], p[0]))
        print(pairs)
        return [word for word, _ in pairs[0:k]]
