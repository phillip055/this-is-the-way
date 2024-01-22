class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = 0
        max_window = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flipped += 1
                while flipped > k:
                    if nums[l] == 0:
                        flipped -=1
                    l += 1
            r += 1            
            max_window = max(max_window, r - l)
        return max_window

