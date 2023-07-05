class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        longest_window = 0
        ptr = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[ptr] == 0:
                    zero_count -= 1
                ptr += 1
        
            longest_window = max(longest_window, i - ptr)
        
        return longest_window
