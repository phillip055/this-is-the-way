# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r, m = 1, n, 0
        while l <= r:
            g = guess(m := (l + r) >> 1)
            if g == -1: r = m - 1
            elif g == 1: l = m + 1
            else: break
        return m

