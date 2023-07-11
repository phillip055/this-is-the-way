class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        flipped = 0
        max_length = float('-inf')

        for right in range(len(nums)):
            if nums[right] == 0:
                flipped += 1
            while flipped > k:
                if nums[left] == 0:
                    flipped -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
            

