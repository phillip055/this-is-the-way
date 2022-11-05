from functools import cache

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        t = Trie()
        for word in wordDict:
            t.add_word(word)
        
        
        @cache
        def dfs(currS, currTrie):
            if not currTrie:
                return False
            if currS == "":
                if currTrie.isEnd:
                    return True
                else:
                    return False
            if currTrie.isEnd:
                s = dfs(currS, t.root) or (dfs(currS[1:], currTrie.children[currS[0]]) if currS[0] in currTrie.children else False)
                return s
            if currS[0] in currTrie.children:
                s = dfs(currS[1:], currTrie.children[currS[0]])
                return s
            else:
                return False
        return dfs(s, t.root)
