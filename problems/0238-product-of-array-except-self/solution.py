class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rights = [1]
        for i in range(1, len(nums)):
            rights.append(nums[i-1] * rights[i-1])
            
        lefts = [1]
        nums.reverse()
        for i in range(1, len(nums)):
            lefts.append(nums[i-1] * lefts[i-1])
        
        lefts.reverse()
        result = []
        print(rights)
        print(lefts)
        for x, y in zip(rights, lefts):
            result.append(x*y)
        return result

