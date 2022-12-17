class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        while tokens:
            token = tokens.pop(0)
            if token not in ["*", "+", "/", "-"]:
                temp.append(token)
            else:
                a = int(temp.pop())
                b = int(temp.pop())
                if token == "*":    
                    res = a*b
                if token == "/":
                    res = int(b/a)
                if token == "+":
                    res = b+a
                if token == "-":
                    res = b-a
                temp.append(res)
        return int(temp[0])
