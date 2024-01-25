class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = [-1]*len(nums)
        for idx, num in enumerate(nums):
            answer[idx] = nums[num]
        return answer
    
