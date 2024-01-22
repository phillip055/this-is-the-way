class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        output = [0] * len(temperatures)
        for idx in range(1, len(temperatures)):
            while len(stack) and temperatures[idx] > stack[-1][0]:
                node = stack.pop()
                output[node[1]] = (idx - node[1])
            stack.append((temperatures[idx], idx))
        return output
        
