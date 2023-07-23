class Solution:
    def arrangeCoins(self, n: int) -> int:
        x = 1
        while ((x + 1) * x) / 2 <= n:
            x += 1
        return x - 1

