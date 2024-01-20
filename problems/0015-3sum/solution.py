class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        targetSum = 0
        nums = sorted(nums)
        results = set()
        for i in range(len(nums)):
            leftIdx = i + 1
            rightIdx = len(nums) - 1
            while leftIdx < rightIdx:
                candidate = nums[leftIdx] + nums[rightIdx] + nums[i]
                if candidate == targetSum:
                    results.add((nums[i], nums[leftIdx], nums[rightIdx])) 
                    leftIdx += 1
                    rightIdx -= 1
                elif candidate > targetSum:
                    rightIdx -= 1
                else:
                    leftIdx += 1
        return results

