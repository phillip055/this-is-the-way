class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _max =max(nums)        
        all_nums = []
        for i in range(max(len(nums), _max)+1):
            all_nums.append(i)
            
        res = set(all_nums) - set(nums)
        res_list = list(res)
        return res_list[0]
