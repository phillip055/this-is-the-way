class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = [(costA - costB,idx) for idx, (costA, costB) in enumerate(costs)]
        diff = sorted(diff)
        b = diff[len(diff)//2:]
        a = diff[:len(diff)//2]
        cost_a = list(map(lambda x: costs[x[1]], a))
        cost_b = list(map(lambda x: costs[x[1]], b))
        _sum = 0
        for _a in cost_a:
            _sum += _a[0]
        for _b in cost_b:
            _sum += _b[1]
        return _sum

