class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """

        import heapq

        piles = [-x for x in piles]

        heapq.heapify(piles)
        

        while k:
            f = heapq.heappop(piles)
            n = f // 2
            heapq.heappush(piles, n)
            k -= 1
        
        return -sum(piles)

        
