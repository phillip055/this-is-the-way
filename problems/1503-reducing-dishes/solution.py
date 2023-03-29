class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        _sum = 0
        max_sum = 0
        for i in range(len(satisfaction)-1, -1, -1):
            if _sum + satisfaction[i] < 0:
                break
            _sum += satisfaction[i]
            max_sum += _sum
        return max_sum
