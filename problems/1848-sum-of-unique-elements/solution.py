class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        _sum = 0
        for k, v in freq.items():
            if v == 1:
                _sum += k
        return _sum

