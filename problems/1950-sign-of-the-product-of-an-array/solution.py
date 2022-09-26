class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_positive = 1
        for num in nums:
            if num < 0:
                is_positive *= -1
            elif num == 0:
                return 0
        return is_positive
