class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def helper(idx):
            if idx == len(cost) - 1:
                return cost[idx]
            if idx >= len(cost):
                return 0
            return cost[idx] + min(helper(idx + 1), helper(idx + 2))

        return min(helper(1), helper(0))

