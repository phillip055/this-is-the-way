class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap, res, minVal = [], 0, 101

        for n in nums:
            if n > 0: res += n
            elif n < 0: heappush(heap, n)
            minVal = min(minVal, abs(n))
        while heap and k > 0:
            res += -heappop(heap)
            k -= 1
        if heap:
            res += sum(heap)
        if k % 2:
            res = res - 2 * minVal
        return res
