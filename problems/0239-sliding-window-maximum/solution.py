class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        l = 0
        output = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.pop(0)
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
        return output
