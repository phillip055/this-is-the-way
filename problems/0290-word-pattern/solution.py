from collections import defaultdict

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        p_char = list(pattern)
        s_word = s.split()

        if len(p_char) != len(s_word):
            return False
        
        table = {}
        table_inv = {}
        for i, j in zip(p_char, s_word):
            if i in table:
                if table[i] != j:
                    return False
                else:
                    continue
            if j in table_inv:
                if table_inv[j] != i:
                    return False
                else:
                    continue
            table[i] = j
            table_inv[j] = i
        return True

            
