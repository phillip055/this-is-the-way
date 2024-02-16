class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        current_number = 0

        for char in s:
            if char == "[":
                stack.append(curr_string)
                stack.append(current_number)
                curr_string = ""
                current_number = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num * curr_string
            elif char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                curr_string += char
        return curr_string
