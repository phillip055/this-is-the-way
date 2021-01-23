class Solution:
    def isValid(self, s: str) -> bool:
        opposites = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        state = []
        for bracket in s:
            if (bracket in ['[', '(', '{']):
                state.append(bracket)
            else:
                if (len(state)) > 0:
                    to_close = state.pop()
                    if (opposites[to_close] != bracket):
                        return False
                else:
                    return False
        return len(state) == 0
