class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        
        currentWords = []
        currentWordsLength = 0
        for word in words:
            if currentWordsLength + len(word) + (len(currentWords) -1) >= maxWidth:
                result.append(currentWords)
                currentWords = []
                currentWordsLength = 0
            currentWords.append(word)
            currentWordsLength += len(word)
        for res in result:
            length = sum(len(s) for s in res)
            remaining = maxWidth - length
            if len(res) == 1:
                res[0] += remaining * " "
                continue
            i = 0
            while remaining > 0:
                _i = i % len(res) 
                if _i == len(res) - 1:
                    i += 1
                    continue
                i += 1
                remaining -= 1
                res[_i] += " "
          
        r = ["".join(res) for res in result]
        if len(currentWords):
            c = " ".join(currentWords)
            length = len(c)
            remaining = maxWidth - length
            c += remaining * " "
            r.append(c)
        return r
            
            
        
