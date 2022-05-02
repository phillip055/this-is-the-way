# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        firstIdx = 1
        lastIdx = n
        while firstIdx < lastIdx:
            pivot = firstIdx + (lastIdx-firstIdx) //2
            res = isBadVersion(pivot)
            if not res:
                firstIdx = pivot + 1
            else:
                lastIdx = pivot
        return lastIdx
                
        
