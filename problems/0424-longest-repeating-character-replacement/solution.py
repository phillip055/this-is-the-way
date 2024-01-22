class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        kv = {}
        most_frequent = 0
        l = 0
        max_len = 0
        for r, char in enumerate(s):
            kv[char] = kv.get(char, 0) + 1 
            most_frequent = max(most_frequent, kv[char])
            if (r - l + 1) - most_frequent > k:
                kv[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
        return max_len

