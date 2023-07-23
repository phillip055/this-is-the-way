import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<3:
            return max(nums)
        n=[-i for i in nums]
        heapq.heapify(n)
        poping=heapq.heappop(n)
        poping=heapq.heappop(n)
        return heapq.heappop(n) * -1

