class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        closest = None
        for idx in range(len(nums) - 2):
            remaining = target - nums[idx]
            low, high = idx + 1, len(nums) - 1
            while low < high:
                candidate = nums[low] + nums[high] + nums[idx]
                if abs(candidate - target) < min_diff:
                    closest = candidate
                    min_diff = abs(candidate - target)
                if candidate == target:
                    return candidate
                elif candidate > target:
                    high -= 1
                else:
                    low += 1
        return closest
                    

