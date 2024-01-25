class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        idx1, idx2, idx3 = 0, 0, 0
        result = []
        while len(arr1) and len(arr2) and len(arr3):
            if arr1[idx1] == arr2[idx2] == arr3[idx3]:
                result.append(arr1[0])
                arr1.pop(0)
                arr2.pop(0)
                arr3.pop(0)
            else:
                item = min(arr1[idx1], arr2[idx2], arr3[idx3])
                if arr1[0] == item:
                    arr1.pop(0)
                if arr2[0] == item:
                    arr2.pop(0)
                if arr3[0] == item:
                    arr3.pop(0)
        return result

