class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        def expand(s, i, j):
            while i > 0 and j < len(s)-1:
                if s[i-1] == s[j+1]:
                    i -= 1
                    j += 1
                else:
                    break
            return i,j
        
        maxI, maxJ = 0,0
        
        for i in range(len(s)-1):
            res1 = expand(s, i, i)
            if s[i] == s[i+1]:
                res2 = expand(s, i, i+1)
                res = max(res1, res2, key=lambda x: x[1]-x[0])
            else:
                res = res1
            if res[1] - res[0] > maxJ - maxI:
                maxJ = res[1]
                maxI = res[0]
        return s[maxI:maxJ+1]
                
                
            
