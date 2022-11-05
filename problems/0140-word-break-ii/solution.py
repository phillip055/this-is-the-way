class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def Trie(words):
            table = {}
            for word in words:
                temp_table = table
                for c in word:
                    if c in temp_table:
                        temp_table = temp_table[c]
                    else:
                        temp_table[c] = {}
                        temp_table = temp_table[c]
                temp_table["*"] = word
            return table
        t = Trie(wordDict)
        result = list()
        def dfs(currS, currTrie, currSentence):
            print(currS, currTrie, currSentence)
            if currS == "":
                if "*" in currTrie:
                    currSentence.append(currTrie["*"])                    
                    result.append(currSentence)
                    return
                else:
                    return
            if "*" in currTrie:
                tempSentence = currSentence[:]
                tempSentence.append(currTrie["*"])
                dfs(currS, t, tempSentence)

            if currS[0] in currTrie:
                nextTrie = currTrie[currS[0]]
                dfs(currS[1:], nextTrie, currSentence[:])
                return
        
        dfs(s, t, [])
        return map(lambda x: " ".join(x), result)
        
        
        
        
