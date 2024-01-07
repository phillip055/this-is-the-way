class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        map = {}

        for i in range(n):
            temp = nums[i]
            if temp not in map:
                map[temp] = []
            map[temp].append(i)
            total_sum = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                a = 2 * nums[i] - nums[j]
                if a in map:
                    for k in map[a]:
                        if k < i:
                            dp[i][j] += dp[k][i] + 1
                        else:
                            break
                total_sum += dp[i][j]
        return total_sum
