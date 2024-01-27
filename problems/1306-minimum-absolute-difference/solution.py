class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diffs = defaultdict(list)
        for idx in range(1, len(arr)):
            diffs[abs(arr[idx-1] - arr[idx])].append((arr[idx-1], arr[idx]))
        print(diffs)
        
        min_diff = sorted(diffs)[0]
        print(min_diff)
        return diffs[min_diff]

