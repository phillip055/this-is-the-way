class Solution:
    def maxArea(self, height: List[int]) -> int:
        f, s = 0, len(height) - 1
        res = 0
        while f < s:
            res = max((s-f) * min(height[f], height[s]), res)
            if height[f] < height[s]:
                f += 1
            else:
                s -= 1
        return res
                

