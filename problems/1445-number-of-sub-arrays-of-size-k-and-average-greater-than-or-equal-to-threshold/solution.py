class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        r = k
        count = 0
        window_sum = sum(arr[:k])
        if window_sum / k >= threshold:
            count += 1
        while r < len(arr):
            window_sum -= arr[r-k]
            window_sum += arr[r]
            if window_sum / k >= threshold:
                count += 1
            r += 1
        return count

            


