class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeroes = {}
        for idx, num in enumerate(nums):
            self.non_zeroes[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for idx, num in vec.non_zeroes.items():
            if idx in self.non_zeroes:
                total += vec.non_zeroes[idx] * self.non_zeroes[idx]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
