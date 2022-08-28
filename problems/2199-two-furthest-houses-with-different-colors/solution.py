class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        j = len(colors)-1
        
        diff = 1
        while i < j:
            if colors[i] == colors[j]:
                j -= 1
            else:
                break
        
        diff = j
        
        i = 0
        j = len(colors)-1
        while i < j:
            if colors[i] == colors[j]:
                i += 1
            else:
                break
        return max(diff, j-i)
