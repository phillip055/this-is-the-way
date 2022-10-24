class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0]
        i = 1
        result = [0 for _ in temperatures]
        while i < len(temperatures):
            while len(temp) and temperatures[i] > temperatures[temp[-1]]:
                result[temp[-1]] = i-temp[-1]
                temp.pop()
            temp.append(i)
            i += 1
        return result
