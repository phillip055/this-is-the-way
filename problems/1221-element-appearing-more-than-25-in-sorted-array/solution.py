class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4

        for idx in range(len(arr) - size):
            if arr[idx] == arr[idx+size]:
                return arr[idx]
        return -1

