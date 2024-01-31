class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq = Counter(nums1)
        result = []
        for num in nums2:
            if num in num1_freq:
                result.append(num)
                num1_freq[num] -= 1
                if num1_freq[num] == 0:
                    del num1_freq[num]
        return result
