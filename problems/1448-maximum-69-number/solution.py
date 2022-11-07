class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = list(str(num))
        
        cmax = 0
        
        for idx in range(len(s)):
            temp = s[idx]
            if temp == '6':
                s[idx] = '9'
                cmax = max(int("".join(s)), cmax)
                break
        return cmax or num

