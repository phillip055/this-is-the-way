class Solution:
    def arraySign(self, nums: List[int]) -> int:
        is_positive = True

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                is_positive = not is_positive
        return 1 if is_positive else -1

