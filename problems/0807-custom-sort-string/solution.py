class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordering = {}
        for idx, val in enumerate(order):
            ordering[val] = idx
            
        freq = Counter(s)
        
        ordering = sorted(ordering, key=ordering.get)
        result = ""
        for ch in ordering:
            if ch in freq:
                result += ch * freq[ch]
                del freq[ch]
        
        for k, v in freq.items():
            result += k * v
        return result

