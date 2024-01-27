class Solution:
    def maximumProduct(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return -1
        arr.sort()
        return max(arr[0] * arr[1] * arr[n - 1], 
                   arr[n - 1] * arr[n - 2] * arr[n - 3]) 
 

