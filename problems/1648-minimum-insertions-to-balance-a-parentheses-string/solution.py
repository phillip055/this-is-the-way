class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "#")

        need = 0
        missing = 0
        for char in s:
            if char == "(":
                need += 2
            else:
                if char == ")":
                    missing += 1
                if need > 0:
                    need -= 2
                else:
                    missing += 1
        return missing + need

                

