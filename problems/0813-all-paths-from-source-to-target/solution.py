class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        def rec(i, currentPath, graph):
            if i >= len(graph) - 1:
                currentPath.append(i)
                result.append(currentPath)
                return;
            
            for nextIdx in graph[i]:
                rec(nextIdx, currentPath[:] + [i], graph)
            
            return;
        
        rec(0, [], graph)
        
        return result
                
