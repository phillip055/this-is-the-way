class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if len(arr) == arr[-1]:
            return arr[-1] + k

        start, end = 0, len(arr) - 1
    
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] - (mid + 1) < k:
                start = mid + 1
            else:
                end = mid - 1
        return start + k
        
            

        

