class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        power = 0
        res = 0
        while res < n:
            res = (3 ** power)
            power+=1
            if res == n:
                return True
        return False
