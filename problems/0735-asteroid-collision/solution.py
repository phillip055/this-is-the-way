class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack)>1 and ((stack[-2]>0) and (stack[-1]<0)):
                first, second = stack.pop(),stack.pop()
                if abs(first) != abs(second):
                    if abs(first) > abs(second):
                        stack.append(first)
                    else:
                        stack.append(second)
        return stack

