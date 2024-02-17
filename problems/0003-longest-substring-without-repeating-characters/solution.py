class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_length = 0, 0
        window_elements = set()
        for r in range(len(s)):
            while s[r] in window_elements:
                window_elements.remove(s[l])
                l += 1
            window_elements.add(s[r])
            max_length = max(r - l + 1, max_length)
        return max_length
            

