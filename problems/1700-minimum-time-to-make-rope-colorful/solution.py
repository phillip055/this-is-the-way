class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        idx0 = 0
        result = 0
        while idx0 < len(colors):
            idx1 = idx0
            _max = float('-inf')
            _sum = 0
            count = 0
            while idx1 < len(colors) and colors[idx0] == colors[idx1]:
                _max = max(neededTime[idx1], _max)
                _sum += neededTime[idx1]
                idx1 += 1
                count += 1
            if count > 0:
                result += _sum - _max
            idx0 = idx1
        return result

