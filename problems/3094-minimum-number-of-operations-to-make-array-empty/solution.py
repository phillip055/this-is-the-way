class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ops = 0
        for v in freq.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                ops += v // 3
            else:
                ops += v // 3 + 1
        return ops

