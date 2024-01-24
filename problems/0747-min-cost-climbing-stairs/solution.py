class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        @cache
        def helper(idx):
            if idx > len(costs) - 1:
                return 0
            return costs[idx] + min(
                helper(idx + 1),
                helper(idx + 2),
            )
        return min(helper(0), helper(1))
            

