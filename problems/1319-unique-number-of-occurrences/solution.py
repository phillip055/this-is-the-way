class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        uniq_keys = set(freq.keys())
        uniq_vals = set(freq.values())
        return len(uniq_keys) == len(uniq_vals)
        
