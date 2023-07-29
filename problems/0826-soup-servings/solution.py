class Solution:
    def soupServings(self, n: int) -> float:
        # WTF
        if n >= 4800:
            return 1
        
        @cache
        def helper(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0.0
            if a <= 0 and b > 0:
                return 1.0
            operations = [(-100, 0), (-75, -25), (-50,-50), (-25,-75)]
            return sum([helper(a + operation[0], b + operation[1]) for operation in operations]) / 4
        return helper(n, n)

