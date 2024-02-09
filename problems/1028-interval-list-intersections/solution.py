# Algo
# [[13,23],[24,25]]
# [[8,12],[15,24],[25,26]]


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx0, idx1 = 0, 0
        result = []
        while idx0 < len(firstList) and idx1 < len(secondList):
            first = firstList[idx0]
            second = secondList[idx1]

            if first[1] >= second[0] and first[0] <= second[1]:
                result.append([
                    max(first[0], second[0]),
                    min(first[1], second[1])
                ])
            if first[1] < second[1]:
                idx0 += 1
            else:
                idx1 += 1
        return result


        
