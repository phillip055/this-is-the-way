class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = []
        while len(nums):
            row = []
            _set = set()
            to_remove = []
            for idx in range(len(nums)):
                if nums[idx] not in _set:
                    row.append(nums[idx])
                    to_remove.append(idx)
                    _set.add(nums[idx])
            for r in reversed(to_remove):
                nums.pop(r)
            matrix.append(row)
        return matrix
