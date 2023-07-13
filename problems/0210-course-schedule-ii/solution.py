class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        order = [0] * numCourses
        mapping = defaultdict(list)

        for prerequisite in prerequisites:
            order[prerequisite[0]] += 1
            mapping[prerequisite[1]].append(prerequisite[0])

        queue = []

        for idx in range(len(order)):
            if order[idx] == 0:
                queue.append(idx)

        seq = []
        while len(queue):
            node = queue.pop(0)
            seq.append(node)
            for next_node in mapping[node]:
                order[next_node] -= 1
                if order[next_node] == 0:
                    queue.append(next_node)
        
        return seq if len(seq) == numCourses else []
                
        
