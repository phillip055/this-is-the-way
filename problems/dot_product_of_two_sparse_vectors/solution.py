class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeroes = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.non_zeroes[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for non_zero_idx in vec.non_zeroes:
            if non_zero_idx in self.non_zeroes:
                total += vec.non_zeroes[non_zero_idx] * self.non_zeroes[non_zero_idx]
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)