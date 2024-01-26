from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        a: list(int) = [int(number) for number in date1.split("-")]
        b: list(int) = [int(number) for number in date2.split("-")]

        a: float = datetime(*a).timestamp()
        b: float = datetime(*b).timestamp()

        return int(abs(a - b) / 86400)