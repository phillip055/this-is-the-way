class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_array = list(str(x))
        return x_array == x_array[::-1]
