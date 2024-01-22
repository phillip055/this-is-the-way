class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = freq.most_common(k)
        return list(map(lambda x: x[0], result))

