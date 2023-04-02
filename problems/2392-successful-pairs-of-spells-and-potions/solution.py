class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []

        m = len(potions)
        maxPotion = potions[m - 1]

        for spell in spells:
            minPotion = (success + spell - 1) // spell
            if minPotion > maxPotion:
                answer.append(0)
                continue
            index = bisect.bisect_left(potions, minPotion)
            answer.append(m - index)

        return answer

        

