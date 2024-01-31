class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        revert = {"1": "1", "6": "9", "9": "6", "8":"8", "0":"0"}
        if len(num) == 0:
            return True        
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] in revert and revert[num[l]] == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    
