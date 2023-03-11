"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for emp in employees:
            table[emp.id] = (emp.importance, emp.subordinates)
        
        exploring = [id]
        importance = 0
        while len(exploring):
            node = exploring.pop(0)
            employeeInfo = table[node]
            importance += employeeInfo[0]
            exploring.extend(employeeInfo[1])
        return importance

