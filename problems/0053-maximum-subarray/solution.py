class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_window = -math.inf
        
        window_sum = 0
        window_start = 0
        
        for window_end in range(len(nums)):    
            window_sum += nums[window_end]
            if window_sum > max_window:
                max_window = window_sum
            while (window_sum < 0):
                window_sum -= nums[window_start]
                window_start+=1
        return max_window
