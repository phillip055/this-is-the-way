class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        _sum = 0
        _product = 1
        for digit in n:
            _sum += int(digit)
            _product *= int(digit)
        return _product - _sum
