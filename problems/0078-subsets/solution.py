class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        for e in nums:
            result += [curr + [e] for curr in result]
        return result
    
