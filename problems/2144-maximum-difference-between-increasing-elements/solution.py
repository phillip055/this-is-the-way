class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        currMin = float('inf')
        diff = float('-inf')
        for num in nums:
            if num > currMin:
                diff = max(num-currMin, diff)
            currMin = min(currMin, num)
            
        return diff if diff != float('-inf') else -1
        
