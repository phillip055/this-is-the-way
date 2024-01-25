class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        prev = float('-inf')
        max_length = 0
        curr_length = 0
        for num in nums:
            if num > prev:
                curr_length += 1
            else:
                curr_length = 1
            prev = num
            max_length = max(max_length, curr_length)
        return max_length
        
