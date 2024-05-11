class Solution:
    def minCost(
        self, n: int, roads: List[List[int]], appleCost: List[int], k: int
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for city_a, city_b, cost in roads:
            graph[city_a - 1].append((city_b - 1, cost))
            graph[city_b - 1].append((city_a - 1, cost))

        def shortest_path(start_city, graph):
            travel_costs = [float("inf") for _ in range(n)]
            travel_costs[start_city] = 0
            heap = [(0, start_city)]
            min_cost = float("inf")

            while heap:
                travel_cost, curr_city = heapq.heappop(heap)
                min_cost = min(min_cost, appleCost[curr_city] + (k + 1) * travel_cost)
                for neighbor, cost in graph[curr_city]:
                    next_cost = travel_cost + cost
                    if next_cost < travel_costs[neighbor]:
                        travel_costs[neighbor] = next_cost
                        heapq.heappush(heap, (next_cost, neighbor))

            return min_cost
        ans = []
        for start_city in range(0, n):
            ans.append(shortest_path(start_city, graph))
        return ans

