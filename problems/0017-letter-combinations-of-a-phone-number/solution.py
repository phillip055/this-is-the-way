class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []        
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def p(current, i, digits):
            if i >= len(digits):
                if current != "":
                    return result.append(current)
            else:
                for m in d[digits[i]]:
                    p(current + m, i+1, digits)
        p("", 0, digits)
        return result
