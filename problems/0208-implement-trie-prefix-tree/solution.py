from collections import defaultdict
class Trie:
    table = {}
    def __init__(self):
        self.table = {}

    def insert(self, word: str) -> None:
        t = self.table
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['*'] = word

    def search(self, word: str) -> bool:
        t = self.table
        for c in word:
            if c in t:
                t = t[c]
            else:
                return False
        return "*" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.table
        for c in prefix:
            if c in t:
                t = t[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
