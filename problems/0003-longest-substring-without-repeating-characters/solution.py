class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        i = 0
        j = 0
        ans = 0
        n = len(s)
        while i<n and j<n:
            if not s[j] in res:
                res.add(s[j])
                j += 1
                ans = max(ans, j-i)
            else:
                res.remove(s[i])
                i += 1
        return ans
            
            
            
            
        
