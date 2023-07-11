class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        _max = prefix_sum
        for g in gain:
            prefix_sum += g
            _max = max(_max, prefix_sum)            
        return _max

