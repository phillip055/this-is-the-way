class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_nums = {"6": "9", "9":"6", "8": "8", "0": "0", "1": "1"}

        result = ""
        for e in reversed(num):
            if e in rotated_nums:
                result += rotated_nums[e]
            else:
                return False

        return result == num
