class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mappings = defaultdict(list)

        explored = set()
        for i,e in enumerate(arr):
            mappings[e].append(i)
        
        def bfs(idx):
            minFound = float('inf')
            nodes = [(idx, 0)]
            while len(nodes):
                nodeIdx, count = nodes.pop(0)
                if nodeIdx in explored:
                    continue
                if nodeIdx == len(arr) - 1:
                    minFound = min(minFound, count)
                    continue
                else:
                    explored.add(nodeIdx)
                if nodeIdx - 1 >= 0:
                    if nodeIdx - 1 in explored:
                        None
                    else:
                        nodes.append((nodeIdx-1, count+1))
                if nodeIdx + 1 <= len(arr) - 1:
                    if nodeIdx + 1 in explored:
                        None
                    else:
                        nodes.append((nodeIdx+1, count+1))
                possibleNextSteps = mappings[arr[nodeIdx]]
                for jumpIdx in possibleNextSteps:
                    if jumpIdx in explored and jumpIdx != nodeIdx:
                        continue
                    nodes.append((jumpIdx, count+1))
                mappings[arr[nodeIdx]] = []
            return minFound
        r = bfs(0)
        return r if r != float('inf') else -1

