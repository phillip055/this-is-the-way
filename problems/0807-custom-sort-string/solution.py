class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = []
        for o in order:
            if o in freq:
                result.append(o*freq[o])
                del freq[o]
        for k, v in freq.items():
            result.append(k*v)
        return "".join(result)

        
