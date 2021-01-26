class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        myset = set(candyType)
        mylist = list(myset)
        
        allowedCandies = len(candyType)/2
        
        return int(min(allowedCandies, len(mylist)))
                
