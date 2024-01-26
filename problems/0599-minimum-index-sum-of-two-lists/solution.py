class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        freq = defaultdict(list)
        
        for idx, v in enumerate(list1):
            freq[v].append(idx)
        
        for idx, v in enumerate(list2):
            freq[v].append(idx)
        
        scores = defaultdict(int)
        
        for k, v in freq.items():
            if len(v) == 2:
                scores[k] += sum(v)
        
        lowest = min(scores.values())
        result = []
        for k, v in scores.items():
            if v == lowest:
                result.append(k)
        return result

