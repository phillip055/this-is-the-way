class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        left_prefix = [0]
        for idx in range(1, len(nums)):
            left_prefix.append(left_prefix[idx-1] + nums[idx-1])

        nums.reverse()
        
        right_prefix = [0]
        for idx in range(1, len(nums)):
            right_prefix.append(right_prefix[idx-1] + nums[idx-1])
        right_prefix.reverse()

        result = []
        for x, y in zip(left_prefix, right_prefix):
            result.append(abs(x-y))
        return result
        
