class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        min_window_sum = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_window_sum = min(min_window_sum, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return min_window_sum if min_window_sum != float('inf') else 0


