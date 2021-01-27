import math 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = math.factorial(n)
        items = list(str(r))
        count = 0
        items.reverse()
        for i in items:
            if i == '0':
                count +=1
            else:
                return count
