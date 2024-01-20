class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9+7
        dp = [0] * n
        s = []
        ans = 0
        for i in range(n):
            while len(s) > 0 and arr[i] <= arr[s[-1]]:
                s.pop()
            if len(s) > 0:
                j = s[-1]
                dp[i] = dp[j] + arr[i] * (i-j)
            else:
                dp[i]= arr[i] * (i+1)
            s.append(i)
            ans = (ans + dp[i]) % mod
        return ans

