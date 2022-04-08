class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        result = []
        for idx in range(len(strs)):
            current_word = strs[idx]
            code = sorted(current_word)
            codestr = "".join(code)
            if codestr in words:
                anagramIdx = words[codestr]
                result[anagramIdx].append(current_word)
            else:
                current_length = len(result)
                words[codestr] = current_length
                result.append([current_word])
        return result
