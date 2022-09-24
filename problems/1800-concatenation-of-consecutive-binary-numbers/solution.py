class Solution:
    def concatenatedBinary(self, n: int) -> int:
        _str = ""
        for i in range(1, n+1):
            _str += str(format(i, "b"))
        
        return int(_str,2)%(10**9 + 7)
