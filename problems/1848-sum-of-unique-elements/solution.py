class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        result = 0
        for k, v in freq.items():
            if v == 1:
                result += k
        return result
        
