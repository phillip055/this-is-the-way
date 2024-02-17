class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        while len(nums):
            node = nums.pop()
            streak = 1
            cursor = node
            while cursor - 1 in nums:
                cursor = cursor - 1
                nums.remove(cursor)
                streak += 1
            cursor = node
            while cursor + 1 in nums:
                cursor = cursor + 1
                nums.remove(cursor)
                streak += 1
            max_length = max(streak, max_length)
        return max_length

