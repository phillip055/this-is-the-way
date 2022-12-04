class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counter = Counter(s)
            
        sortedKeys = sorted(counter, key=lambda x: counter[x], reverse=True)
        print(sortedKeys)
        result = ""
        for e in sortedKeys:
            result += e * counter[e]
        return result

