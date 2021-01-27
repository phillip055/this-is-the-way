class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        while(n >= 1):
            x = n % 10
            sum += x**2
            n = n // 10
        if(sum == 1 or sum == 7):
            return True
        elif(sum < 10):
            return False
        else:
            return self.isHappy(sum)
