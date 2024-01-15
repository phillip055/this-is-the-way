class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played = set()
        losses = Counter()
        for winner, loser in matches:
            played.add(winner)
            played.add(loser)
            losses[loser] += 1
        
        once = filter(lambda loser: losses[loser] == 1, losses.keys())
        undefeated = played - set(losses.keys())
        once = sorted(list(once))
        undefeated = sorted(list(undefeated))
        return [undefeated, once]

