class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        gas = nums[0]
        for station in nums:
            if gas == 0:
                return False
            gas -= 1
            gas = max(gas, station)
        return True

