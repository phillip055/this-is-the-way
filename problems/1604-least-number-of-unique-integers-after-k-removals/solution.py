class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        pq = [(v, key) for key, v in freq.items()]
        pq = sorted(pq)
        count = 0
        while k >= 0 and len(pq) > 0:
            v, _ = pq.pop(0)
            if k < v:
                return len(pq) + 1
            else:
                k -= v
                count += 1
        return len(arr) - count


