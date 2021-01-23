class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if len(words) > 0 else 0
        
        
