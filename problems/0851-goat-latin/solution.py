class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        
        for idx in range(len(words)):
            word = words[idx] 
            if word[0] not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                first = word[0]
                word = word[1:]
                word += first
            word += "ma"
            word += "a"*(idx+1)
            words[idx] = word
        return " ".join(words)
                

