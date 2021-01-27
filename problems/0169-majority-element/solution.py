class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        _dict = {}
        majority = len(nums)/2
        for num in nums:
            if (num in _dict):
                _dict[num]+=1
                if (_dict[num] > majority):
                    return num
            else:
                _dict[num] = 1
