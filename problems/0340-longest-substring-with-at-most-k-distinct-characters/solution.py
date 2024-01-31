class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        freq = Counter()
        longest_length = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while len(freq.keys()) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            longest_length = max(longest_length, r - l + 1)
        return longest_length
                
