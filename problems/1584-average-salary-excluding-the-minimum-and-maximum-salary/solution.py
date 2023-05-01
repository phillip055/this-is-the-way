class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        salary.pop()
        salary.pop(0)
        return sum(salary) / len(salary)

