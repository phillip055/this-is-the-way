class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right):
            if left == right:
                return nums[left]
            choose_left = nums[left] - helper(left + 1, right)
            choose_right = nums[right] - helper(left, right - 1)
            return max(choose_left, choose_right)
        return helper(0, len(nums)-1) >= 0

