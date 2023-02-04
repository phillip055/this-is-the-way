class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        ptr1 = 0
        ptr2 = size
        word1 = Counter(s1)
        while ptr2 < len(s2) + 1:
            currentWord = Counter(s2[ptr1:ptr2])
            invalid = False
            print(currentWord)
            print(word1)
            for i in word1:
                if word1[i] != currentWord[i]:
                    invalid = True
                    break
            if not invalid:
                return True
            ptr1 += 1
            ptr2 += 1
        return False
            

