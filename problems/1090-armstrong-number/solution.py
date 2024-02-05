class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = list(map(int, list(str(n))))
        k = len(digits)
        _sum = 0
        for digit in digits:
            _sum += digit ** k
        return _sum == n

