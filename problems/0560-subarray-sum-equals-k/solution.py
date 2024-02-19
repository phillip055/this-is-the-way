class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(lambda : 0)
        prefix_sums[0] = 1 
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            count += prefix_sums[diff]
            prefix_sums[prefix_sum] += 1
        return count

