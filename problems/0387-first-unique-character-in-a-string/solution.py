class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        
        uniq_elements = {}
        for k, v in freq.items():
            if v == 1:
                uniq_elements[k] = v
        
        
        for idx, ch in enumerate(list(s)):
            if ch in uniq_elements:
                return idx
        return -1
        
        
        
