class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in res:
                return [res[missing], i]
            else:
                res[nums[i]] = i
