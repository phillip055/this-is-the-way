class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(lambda : 0)
        prefix_sums[0] = 1
        curr = 0
        result = 0
        for num in nums:
            curr += num
            diff = curr - k
            result += prefix_sums[diff]
            prefix_sums[curr] += 1
        return result


