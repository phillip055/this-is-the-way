from collections import defaultdict

class WordDictionary:
    def __init__(self):
        self.trie = defaultdict()

    def addWord(self, word: str) -> None:
        current_trie = self.trie
        for char in word:
            if char not in current_trie:
                current_trie[char] = {}
            current_trie = current_trie[char]
        current_trie["*"] = word

    def search(self, word: str) -> bool:
        def dfs(trie, idx):
            if len(word) == idx:
                return "*" in trie
            if type(trie) == str:
                return False
            if word[idx] in trie:
                if dfs(trie[word[idx]], idx+1):
                    return True
            if word[idx] == ".":
                for next_trie in trie.values():
                    if dfs(next_trie, idx+1):
                        return True
            return False
        return dfs(self.trie, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
