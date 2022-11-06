class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        
        tokens = []
        
        currentToken = ""
        for e in s:
            if e in ["*", "+", "/", "-"]:
                currentToken = int(currentToken)
                if tokens and tokens[-1] == "-":
                    tokens.pop()
                    currentToken *= -1
                tokens.append(currentToken)
                if e != "+":
                    tokens.append(e)
                currentToken = ""
            else:
                currentToken += e
        if currentToken:
            currentToken = int(currentToken)
            if tokens and tokens[-1] == "-":
                tokens.pop()
                currentToken *= -1
            tokens.append(currentToken)
            
        idx = 0
        stack = []
        while idx < len(tokens):
            if tokens[idx] in ["*", "/"]:
                if tokens[idx] == "*":
                    recentToken = stack.pop()
                    result = recentToken * tokens[idx + 1]
                    stack.append(result)
                if tokens[idx] == "/":
                    recentToken = stack.pop()
                    result = int(recentToken / tokens[idx + 1])
                    stack.append(result)
                idx += 2
                continue
            else:
                stack.append(tokens[idx])
                idx += 1
        return sum(stack)
        
