class Solution:
    def numDecodings(self, s):
        mapping = set()
        for idx in range(1,27):
            mapping.add(str(idx)) 
        
        @cache
        def helper(s):
            if len(s) == 0:
                return 1
            if s[0] == "0":
                return 0
            c = 0
            if s[0] in mapping:
                c += helper(s[1:])
            if len(s) > 1 and s[:2] in mapping:
                c += helper(s[2:])
            return c
        return helper(s)

