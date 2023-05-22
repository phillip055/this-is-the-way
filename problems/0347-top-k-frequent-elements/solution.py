class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        f = sorted(c, key=lambda x: c[x], reverse=True)
        return f[:k]
