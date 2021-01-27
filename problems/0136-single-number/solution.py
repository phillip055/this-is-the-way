class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        
        for num in nums:
            if (num in s):
                s.remove(num)
            else:
                s.add(num)
        
        return list(s)[0]
            
