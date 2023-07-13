class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        order = [0] * numCourses
        mapping = [[] for _ in range(numCourses)]
        
        for prerequisite in prerequisites:
            order[prerequisite[0]] += 1
            mapping[prerequisite[1]].append(prerequisite[0])
        
        queue = []
        visited = set()

        for idx in range(len(order)):
            if order[idx] == 0:
                queue.append(idx)
        
        while len(queue):
            node = queue.pop(0)
            visited.add(node)
            for next_node in mapping[node]:
                order[next_node] -= 1
                if order[next_node] == 0:
                    queue.append(next_node)
        return len(visited) == numCourses
    
