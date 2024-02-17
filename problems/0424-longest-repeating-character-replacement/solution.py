class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_length, max_freq = 0, 0, 0
        freq = defaultdict(lambda : 0)
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_length = max(r - l + 1, max_length)
        return max_length

