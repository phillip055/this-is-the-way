class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            num = num * 10 + pop
            a = int(a/10)
        if (x>0) and num < 2**31:
            return num
        elif x<0 and num <= 2**31:
            return -num
        else:
            return 0
        
