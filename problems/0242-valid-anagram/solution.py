class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        t_list.sort()
        s_list.sort()
        return t_list == s_list
