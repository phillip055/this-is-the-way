class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x * x, n//2)
            else:
                return x * self.myPow(x, n - 1)
        else:
            return 1/self.myPow(x, -1*n)

