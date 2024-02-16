class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def helper(idx):
            if idx > len(nums) - 1:
                output.append(subset.copy())
                return
            
            subset.append(nums[idx])
            helper(idx + 1)
            subset.pop()
            helper(idx + 1)
        helper(0)
        return output

