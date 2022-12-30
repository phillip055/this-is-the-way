class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        toFind = len(graph) - 1
        result = []
        def dfs(node, visited=[]):
            print(visited)
            if node == toFind:
                visited.append(node)
                result.append(visited)
                return True
            if node in visited:
                return
            visited.append(node)
            nextNodes = graph[node]
            for n in nextNodes:
                dfs(n, list(visited))
        
        dfs(0)
        return result


