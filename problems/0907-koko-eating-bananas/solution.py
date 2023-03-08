import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles = sorted(piles)
        
        l, r = 1, max(piles)


        def calc(k, piles):
            return sum(list(map(lambda x: math.ceil(x/k), piles)))

        ans = -1

        while l <= r:
            mid = l + ((r-l)//2)
            res = calc(mid, piles)
            if res <= h:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
            

            


