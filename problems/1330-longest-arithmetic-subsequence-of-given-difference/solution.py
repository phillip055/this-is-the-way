class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        tracker = {}

        for a in arr:
            if a - difference in tracker:
                tracker[a] = tracker[a-difference] + 1
            else:
                tracker[a] = 1
            
        return max(tracker.values())

