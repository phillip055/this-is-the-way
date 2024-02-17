class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while len(stack) and stack[-1][0] < temp:
                t, i = stack.pop()
                result[i] = idx - i
            stack.append((temp, idx))
        return result        

