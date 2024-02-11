class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max = 0
        window = set()
        left = 0
        for right in range(len(s)):
            if s[right] in window:
                while s[left] != s[right]:
                    if s[left] in window:
                        window.remove(s[left])
                    left += 1
                left += 1
            window.add(s[right])
            _max = max(len(window), _max)
        return _max


