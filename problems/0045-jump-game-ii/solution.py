class Solution:
    def jump(self, nums: List[int]) -> int:
        minDP = [float('inf') for _ in nums]
        minDP[-1] = 0
        finalPos = len(nums) - 1
        for idx in range(len(nums) - 1, -1, -1):
            for jumpSize in range(1, nums[idx]+1):
                to = jumpSize + idx
                maxToNeeded = min(finalPos, to)
                minDP[idx] = min(1 + minDP[maxToNeeded], minDP[idx])
        return minDP[0]
                
            
