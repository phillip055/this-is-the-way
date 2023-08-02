class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for idx in range(len(nums)):
            fixed_val = nums.pop(idx)
            result = self.permute(nums[:])
            for r in result:
                r.insert(0, fixed_val)
                res.append(r)
            nums.insert(idx, fixed_val)
        return res

