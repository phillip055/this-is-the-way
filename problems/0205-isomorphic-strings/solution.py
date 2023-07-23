class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        inverse_mapping = {}
        for x,y in zip(s, t):
            if x not in mapping and y not in inverse_mapping:
                mapping[x] = y
                inverse_mapping[y] = x
            elif x not in mapping or y not in inverse_mapping:
                return False
            if mapping[x] != y and inverse_mapping[y] != x:
                return False
        return True

