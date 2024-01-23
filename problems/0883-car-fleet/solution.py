class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        def turns(position, speed):
            return (target - position) / speed
        
        sorted_cars = sorted(zip(positions, speeds), reverse=True)
        
        turns = list(map(lambda x: turns(x[0], x[1]), sorted_cars))
        
        stack = [turns[0]]
        
        for turn in turns:
            if turn > stack[-1]:
                stack.append(turn)

        return len(stack)
                

