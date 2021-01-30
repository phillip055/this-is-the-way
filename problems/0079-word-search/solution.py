class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        # dp = [[-1 for val in range(len)]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    int_ans = Solution.recur(board=board, word=word, ind=1, row=i, col=j)
                    ans = ans or int_ans
                    if ans == True:
                        return True
        return ans
    
    @staticmethod
    def recur(board, word, ind, row, col):
        if ind == len(word):
            return True
        
        ans = False
        char = board[row][col]
        board[row][col] = '#'
        for neigh in [[-1,0],[1,0],[0,-1],[0,1]]:
            new_row = row + neigh[0]
            new_col = col + neigh[1] 
            if new_row >=0 and new_row < len(board) and new_col >=0 and new_col < len(board[0]):
                if board[new_row][new_col] == word[ind]:
                    ans = ans or Solution.recur(board, word, ind + 1, new_row, new_col)
        board[row][col] = char
        return ans
