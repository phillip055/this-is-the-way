class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        
        
        def rec(i, curr, total):
            if total > target or i >= len(candidates):
                return;
            if sum(curr) == target:
                result.append(curr[:])
                return
            
            curr.append(candidates[i])
            rec(i, curr, total+candidates[i])
            curr.pop()
            rec(i+1, curr, total)
            
        rec(0, [], 0)
        return result
