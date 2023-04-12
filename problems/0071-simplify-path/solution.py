class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")

        stack = []
        for token in tokens:
            if token == "" or token == ".":
                continue
            if token == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(token)
        return "/" + "/".join(stack)

