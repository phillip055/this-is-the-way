class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        
        grid = ["" for _ in range(numRows)]
        
        rowIdx, idx = 0, 0
        diagonal = -1
        while idx < len(s):
            grid[rowIdx%(numRows)] += s[idx]
            
            if diagonal == 1:
                rowIdx -= 1
            else:
                rowIdx += 1
                
            idx += 1
            if idx % (numRows - 1) == 0:
                diagonal *= -1
        return "".join(grid)
            
        


