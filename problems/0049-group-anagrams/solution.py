class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        
        for a in strs:
            d = "".join(sorted(a))
            if d in table:
                table[d].append(a)
            else:
                table[d] = [a]
        return [table[k] for k in table]

