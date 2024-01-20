class Solution:
    def maxArea(self, height: List[int]) -> int:
        idx0 = 0
        idx1 = len(height) - 1
        _max = 0
        while idx0 < idx1:
            l = idx1 - idx0
            h = min(height[idx0], height[idx1])
            _max = max(h * l, _max)
            if height[idx1] > height[idx0]:
                idx0 += 1
            else:
                idx1 -= 1
        return _max
