class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        def cost_of_string(s):
            cost = 0
            for idx in range(len(s)):
                cost += ord(s[idx])
            return cost

        @cache
        def helper(i, j):
            if i >= len(s1) and j >= len(s2):
                return 0
            if i >= len(s1) or j >= len(s2):
                return cost_of_string(s1[i:]) + cost_of_string(s2[j:])
            if s1[i] == s2[j]:
                return helper(i + 1, j + 1)
            return min(
                cost_of_string(s1[i: i+1]) + helper(i + 1, j),
                cost_of_string(s2[j: j+1]) + helper(i, j + 1),
                cost_of_string(s1[i: i+1]) + cost_of_string(s2[j: j+1]) + helper(i + 1, j + 1)
            )
        return helper(0,0)

