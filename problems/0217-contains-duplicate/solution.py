class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for num in nums:
            if num in _set:
                return True
            _set.add(num)
        return False
