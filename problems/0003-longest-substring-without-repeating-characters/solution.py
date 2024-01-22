class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_substring = 0
        current_set = set()
        while r < len(s) and l < len(s):
            if not s[r] in current_set:
                current_set.add(s[r])
                r += 1
                longest_substring = max(longest_substring, r-l)
            else:
                current_set.remove(s[l])
                l += 1
        return longest_substring

