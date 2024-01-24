import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_taken(piles, k):
            return sum([math.ceil(pile / k) for pile in piles])
        
        l, r = 1, max(piles)
        ans = -1
        while l <= r:
            mid = l + ((r-l) // 2)
            if time_taken(piles, mid) <= h:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

