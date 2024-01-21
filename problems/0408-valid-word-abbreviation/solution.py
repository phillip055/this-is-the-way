class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx, abbr_idx = 0, 0
        while word_idx < len(word) and abbr_idx < len(abbr):
            current_digit = ""
            while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                current_digit += abbr[abbr_idx]
                abbr_idx += 1

            if len(current_digit):
                if current_digit[0] == "0":
                    return False
                word_idx += int(current_digit)
                continue
            

            if word[word_idx] != abbr[abbr_idx]:
                return False
            word_idx += 1
            abbr_idx += 1
        return word_idx == len(word) and abbr_idx == len(abbr)
                
