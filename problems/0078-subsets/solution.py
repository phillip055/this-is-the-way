class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current = []

        def helper(idx):
            nonlocal current
            if idx > len(nums) - 1:
                subsets.append(current.copy())
                return
            
            current.append(nums[idx])
            helper(idx + 1)
            current.pop()
            helper(idx + 1)
        helper(0)
        return subsets

