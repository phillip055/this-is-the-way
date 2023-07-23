class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for operation in operations:
            if "+" in operation:
                result += 1
            else:
                result -= 1
        return result

