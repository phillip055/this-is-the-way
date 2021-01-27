class Solution:
    def countPrimes(self, n: int) -> int:
        
        if (n < 3):
            return 0
        
        Prime_list = [1] * n
        Prime_list[0] = 0
        Prime_list[1] = 0
        
        for i in range(2,n):
            for j in range (2,n):
                mul = i * j
                if (mul < n):
                    Prime_list[mul] = 0
                else:
                    break
        return (sum(Prime_list))
