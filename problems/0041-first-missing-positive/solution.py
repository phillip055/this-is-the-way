class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = [0] * len(nums)
        for i, v in enumerate(nums):
            if v > len(nums):
                continue
            if v < 0:
                continue
            print(v)
            temp[v-1] = v
        print(nums)
        for i,v in enumerate(temp):
            if i+1 != v:
                return i+1
       
        return len(nums) + 1
