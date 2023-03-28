from functools import cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def dfs(day_index, current_package_end_day):
            if day_index >= len(days):
                return 0
            if days[day_index] <= current_package_end_day:
                return dfs(day_index + 1, current_package_end_day)
            return min(
                costs[0] + dfs(day_index+1, days[day_index]),
                costs[1] + dfs(day_index+1, days[day_index]+6),
                costs[2] + dfs(day_index+1, days[day_index]+29)
            )
        return dfs(0, -1)

