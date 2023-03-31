from functools import cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def has_apple(start_row, start_col, end_row, end_col):
            for r in range(start_row, end_row+1):
                for c in range(start_col, end_col+1):
                    if pizza[r][c] == 'A':
                        return True 
            return False 
        
        @cache
        def dp(start_row, start_col, num_slices_left):

            if num_slices_left == 1:
                if has_apple(start_row, start_col, len(pizza)-1, len(pizza[0])-1):
                    return 1
            
            num_ways = 0 
            for i in range(start_col+1, len(pizza[0])):
                if has_apple(start_row, start_col, len(pizza)-1, i-1):
                    num_ways += dp(start_row, i, num_slices_left-1)
            for j in range(start_row+1, len(pizza)):
                if has_apple(start_row, start_col, j-1, len(pizza[0])-1):
                    num_ways += dp(j, start_col, num_slices_left-1)
            return num_ways 

        return dp(0, 0, k) % (10 ** 9 + 7)

