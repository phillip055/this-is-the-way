class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        
        dp = [0] * (len(profit) + 1)

        for i, (endTime, startTime, profit) in enumerate(jobs):
            index = bisect_right(jobs, startTime, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + profit)
        return dp[len(jobs)]

