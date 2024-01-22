class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        idx0, idx1 = 0, 0
        result = []
        while idx0 < len(firstList) and idx1 < len(secondList):
            if firstList[idx0][1] >= secondList[idx1][0] and firstList[idx0][0] <= secondList[idx1][1]:
                result.append([
                    max(firstList[idx0][0], secondList[idx1][0]), 
                    min(firstList[idx0][1], secondList[idx1][1])
                ])
            if firstList[idx0][1] < secondList[idx1][1]:
                idx0 += 1
            else:
                idx1 += 1
        return result
    
