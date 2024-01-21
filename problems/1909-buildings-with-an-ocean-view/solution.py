class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        idx = len(heights) - 1
        _max = 0
        result = []
        while idx >= 0:
            if heights[idx] > _max:
                result.append(idx)
                _max = max(heights[idx], _max)
            idx -= 1
        result = reversed(result)
        return result

