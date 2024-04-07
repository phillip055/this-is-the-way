class Solution:
    def checkValidString(self, s: str) -> bool:
        asterisks = []
        brackets = []

        for i, char in enumerate(s):
            if char == "(":
                brackets.append(i)
            elif char == "*":
                asterisks.append(i)
            else:
                if len(brackets):
                    brackets.pop()
                elif len(asterisks):
                    asterisks.pop()
                else:
                    return False
        while brackets and asterisks:
            if brackets.pop() > asterisks.pop():
                return False
        return not brackets

                    

