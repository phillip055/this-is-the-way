class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currGas = nums[0]
        for gasIdx in range(1, len(nums)):
            if currGas <= 0:
                return False
            currGas -= 1
            currGas = max(currGas, nums[gasIdx])
        return True

