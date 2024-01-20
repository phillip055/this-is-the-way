class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        eval_stack = []
        while len(tokens):
            token = tokens.pop(0)
            if token in ["+", "-", "/", "*"]:
                s = int(eval_stack.pop())
                f = int(eval_stack.pop())
                if token == "+":
                    eval_stack.append(f+s)
                if token == "-":
                    eval_stack.append(f-s)
                if token == "*":
                    eval_stack.append(f*s)
                if token == "/":
                    eval_stack.append(int(f/s))
            else:
                eval_stack.append(token)
        if len(eval_stack) == 1:
            return int(eval_stack[0])
        return None
