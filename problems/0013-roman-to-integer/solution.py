class Solution:
    def romanToInt(self, s: str) -> int:
        symVal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        _sum = 0
        roman_characters = list(s)
        last_letter = None
        while(roman_characters != []):
            current_letter = roman_characters[-1]
            if (last_letter==None or (symVal[last_letter] <= symVal[current_letter])):
                _sum += symVal[current_letter]
                print('First Case')
            else:
                _sum -= symVal[current_letter]
                print('Second Case')
            last_letter = roman_characters.pop()
        return _sum
