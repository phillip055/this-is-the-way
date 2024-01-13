class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s)-Counter(t)).total()
