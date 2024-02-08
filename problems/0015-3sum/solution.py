class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for idx in range(len(nums)):
            num = nums[idx]
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                candidate = num + nums[left] + nums[right]
                if candidate == 0:
                    result.add((num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif candidate < 0:
                    left += 1
                else:
                    right -= 1
        return list(map(list, result))


