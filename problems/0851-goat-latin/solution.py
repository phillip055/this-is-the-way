class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        result = []
        for idx, word in enumerate(words):
            if word[0] not in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                word = list(word)
                letter = word.pop(0)
                word = "".join(word) + letter    
            word += "ma" + ("a" * (idx + 1))
            result.append(word)
        return " ".join(result)
            
            

