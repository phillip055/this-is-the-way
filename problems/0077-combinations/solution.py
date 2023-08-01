class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        nums = [0] * k

        def helper(position, curr):
            if position == k:
                arr.append(nums[:])
                return
            for idx in range(curr, n - k + position + 2):
                nums[position] = idx
                helper(position + 1, idx + 1)
        helper(0, 1)
        return arr

