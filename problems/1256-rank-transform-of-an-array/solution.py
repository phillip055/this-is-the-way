class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 0
        mapping = {}
        result = []
        for idx, val in enumerate(sorted(arr)):
            if val not in mapping:
                rank += 1
                mapping[val] = rank
        for val in arr:
            result.append(mapping[val])
        return result

