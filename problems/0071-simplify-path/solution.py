class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        stack = []
        for token in tokens:
            if token == "..":
                if len(stack):
                    stack.pop()
                else:
                    continue
            elif token == "." or "" == token:
                continue
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

