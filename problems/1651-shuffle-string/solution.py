class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = dict(zip(indices, s)) # we can use hashmap for storing index of each character
        
        string = "" # current state of string is empty
        
        for i in range(len(indices)): # loop through each index and append corresponding character to end of the string
            string += res[i]
        
        return string
