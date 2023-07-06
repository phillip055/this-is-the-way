class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_idx = 0
        end_idx = 0
        current_sum = 0
        min_window_length = float('inf')

        for end_idx in range(0, len(nums)):
            current_sum += nums[end_idx]

            while current_sum >= target:
                min_window_length = min(min_window_length, end_idx - start_idx + 1)
                current_sum -= nums[start_idx]
                start_idx += 1
        return min_window_length if min_window_length != float('inf') else 0

