class Solution:

    @cache
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if row >= n or column >= n or column < 0 or row < 0:
            return 0
        if k == 0:
            return 1
        possible_moves = [(2,1), (2,-1), (1,2), (1,-2), (-1, 2), (-1,-2), (-2, 1), (-2,-1)]
        probability_sum = 0
        for m in possible_moves:
            probability_sum += self.knightProbability(n, k - 1, row + m[0], column + m[1])
        return probability_sum/len(possible_moves)

