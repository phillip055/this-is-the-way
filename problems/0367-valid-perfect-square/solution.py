class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        idx = 0
        curr = 0
        while curr < num:
            curr = idx * idx
            idx += 1
            if curr == num:
                return True
        return False


