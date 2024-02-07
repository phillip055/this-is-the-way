class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        for idx in range(1, len(nums) - 1):
            if nums[idx] == nums[idx+1]:
                nums[idx] = nums[idx-1]
            if nums[idx-1] < nums[idx] > nums[idx+1]:
                count += 1
            elif nums[idx-1] > nums[idx] < nums[idx+1]:
                count += 1
        return count
        
