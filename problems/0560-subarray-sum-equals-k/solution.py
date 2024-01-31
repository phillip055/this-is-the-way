class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        curr = 0
        prev_sum = defaultdict(lambda : 0)
        for r in range(len(nums)):
            curr += nums[r]
            print(l, r, curr)
            if curr == k:
                count += 1
            if curr - k in prev_sum:
                count += prev_sum[curr - k] 
            prev_sum[curr] += 1
        return count
        
        
