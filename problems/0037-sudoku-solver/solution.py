class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
#          boolean isSafe(int row,int col,char val,char[][] board)
#     {
#         for(int i=0; i<board.length; i++)
#         {
#           //check row
#             if(board[row][i]==val)
#                 return false;
          
#           //check column
#             if(board[i][col]==val)
#                 return false;
          
#           //check 3*3 matrix
#             if(board[3*(row/3)+i/3][3*(col/3)+i%3]==val)
#                 return false;
#         }
#         return true;
#     }

        def isValid(row, col, val):
            for i in range(len(board)):
                if str(val) == board[row][i]: return False
                if str(val) == board[i][col]: return False
                if str(val) == board[3*(row//3) +i//3][3*(col//3) +i%3]: return False
            return True
        
        def solve(i,j):
            if i > len(board) - 1:
                return True
            if j > len(board[0]) - 1:
                return solve(i+1, 0)
            if board[i][j] != ".":
                return solve(i, j+1)
            temp = board[i][j]
            for x in range(1, 10):
                if isValid(i, j, x):
                    board[i][j] = str(x)
                    if solve(i,j+1):
                        return True
            board[i][j] = temp
            return False
        
        solve(0,0)
        
    
                
