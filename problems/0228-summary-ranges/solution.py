class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        def add_to_result(curr_range):
            if curr_range[0] == curr_range[1]:
                return str(curr_range[0])
            else:
                return str(curr_range[0]) + "->" + str(curr_range[1])
        result = []
        curr_range = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            if curr_range[1] + 1 == nums[i]:
                curr_range[1] = nums[i]
            else:
                result.append(add_to_result(curr_range))
                curr_range[0] = nums[i]
                curr_range[1] = nums[i]
        result.append(add_to_result(curr_range))     
        return result

