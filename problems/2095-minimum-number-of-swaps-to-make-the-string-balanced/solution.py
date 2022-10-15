class Solution:
    def minSwaps(self, s: str) -> int:
        maxDiff, count = 0, 0
        for c in s:
            if c == "[":
                count -= 1
            else:
                count += 1
            maxDiff = max(maxDiff, count)
        return (maxDiff + 1) //2
