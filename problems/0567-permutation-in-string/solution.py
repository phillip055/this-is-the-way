class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)
        for idx in range(window_size, len(s2)+1):
            s = s2[idx-window_size: idx]
            if Counter(s) == Counter(s1):
                return True
        return False
