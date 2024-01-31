class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x","y", "z"]
        }
        result = []
        if len(digits) == 0:
            return []
        def helper(idx, digits, path=""):
            if idx >= len(digits):
                result.append(path)
                return
            
            digit = digits[idx]
            for next_char in mapping[digit]:
                helper(idx + 1, digits, path + next_char)
        
        helper(0, digits)
        return result
