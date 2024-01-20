class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(node):
            result = float('inf')
            if node[0] == len(matrix) - 1:
                return matrix[node[0]][node[1]]
            for nextStep in [(1,-1), (1, 0), (1,1)]:
                nextNode = (node[0] + nextStep[0], node[1] + nextStep[1])
                if nextNode[0] >= len(matrix) or nextNode[1] >= len(matrix) or nextNode[0] < 0 or nextNode[1] < 0:
                    continue
                res = matrix[node[0]][node[1]] + dfs(nextNode)
                result = min(res, result)
            return result

        result = float('inf')
        for i in range(len(matrix)):
            res = dfs((0, i))
            result = min(res, result)
        return result

