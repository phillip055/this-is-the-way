class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(M)):
            temp = []
            for j in range(len(M[0])):
                s = [M[i][j]]
                if i - 1 >= 0:
                    s.append(M[i - 1][j])
                    if j - 1 >= 0:
                        s.append(M[i - 1][j - 1])
                    if j + 1 < len(M[0]):
                        s.append(M[i - 1][j + 1])
                if i + 1 < len(M):
                    s.append(M[i + 1][j])
                    if j - 1 >= 0:
                        s.append(M[i + 1][j - 1])
                    if j + 1 < len(M[0]):
                        s.append(M[i + 1][j + 1])
                if j - 1 >= 0:
                    s.append(M[i][j - 1])
                if j + 1 < len(M[0]):
                    s.append(M[i][j + 1])
                temp.append(sum(s) // len(s))
            result.append(temp)
        return result
