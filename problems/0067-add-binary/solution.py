class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idx0 = len(a) - 1
        idx1 = len(b) - 1
        
        carry = 0
        result = []
        while idx0 >= 0 or idx1 >= 0 or carry:
            count = 0
            if idx0 >= 0:
                if a[idx0] == "1":
                    count += 1
                idx0 -= 1
            if idx1 >=0:
                if b[idx1] == "1":
                    count += 1
                idx1 -= 1
            if carry > 0:
                carry -= 1
                count += 1
            
            if count == 0:
                result.append("0")
            if count == 1:
                result.append("1")
            if count == 2:
                result.append("0")
                carry += 1
            if count == 3:
                result.append("1")
                carry += 1
        return "".join(reversed(list(result)))
