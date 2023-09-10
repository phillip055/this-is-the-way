class Solution:

    @cache
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        count = (self.countOrders(n - 1) * (2 * n - 1) * n)
        return count % (10**9+7)
    
