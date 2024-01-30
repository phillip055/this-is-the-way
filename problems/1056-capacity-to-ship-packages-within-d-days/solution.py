class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(weights, capacity, days):
            days_taken = 0
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > capacity:
                    curr_weight = weight
                    days_taken += 1
                else:
                    curr_weight += weight
            print(capacity, days_taken)
            return days_taken < days
            
                
        max_weight = 0
        total_weight = 0
        for weight in weights:
            max_weight = max(max_weight, weight)
            total_weight += weight
        l, r = max_weight, total_weight
        while l < r:
            mid = (l + r) // 2
            if feasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1
        return l

