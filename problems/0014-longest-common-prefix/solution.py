class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = map(lambda string: len(string), strs)
        lengths_list = list(lengths)
        min_length = min(lengths_list) if lengths_list != [] else 0
        res = ''
        for i in range(min_length):
            current_value = None
            for _str in strs:
                x = _str[i]
                if current_value == None:
                    current_value = x
                elif x != current_value:
                    return res
            res += current_value
        return res
