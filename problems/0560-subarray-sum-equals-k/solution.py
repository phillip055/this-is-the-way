class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(lambda : 0)
        prefixSums[0] = 1
        currSum = 0
        result = 0
        for num in nums:
            currSum += num
            diff = currSum - k
            result += prefixSums[diff]
            prefixSums[currSum] += 1
        return result

