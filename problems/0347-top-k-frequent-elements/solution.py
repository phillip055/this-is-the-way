class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = Counter(nums)
        f = sorted(r, key=r.get, reverse=True)
        return f[:k]
