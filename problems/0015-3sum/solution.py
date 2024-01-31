class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        in_result = set()
        for idx in range(len(nums) - 2):
            total = nums[idx]
            l, r = idx + 1, len(nums) - 1
            while l < r:
                candidate = total + nums[l] + nums[r]
                if candidate == 0:
                    if (total, nums[l], nums[r]) not in in_result:
                        result.append([total, nums[l], nums[r]])
                        in_result.add((total, nums[l], nums[r]))
                    r -= 1
                if candidate > 0:
                    r -= 1
                else:
                    l += 1
        return result

