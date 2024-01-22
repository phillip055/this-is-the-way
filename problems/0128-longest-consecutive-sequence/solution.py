class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        max_seq = float('-inf')
        while len(nums):
            num = nums.pop()
            streak = 1
            curr = num
            while curr - 1 in nums:
                nums.remove(curr-1)
                streak += 1
                curr -= 1
            curr = num
            while curr + 1 in nums:
                nums.remove(curr+1)
                streak += 1
                curr += 1
            max_seq = max(max_seq, streak)
        return max_seq
            

            

