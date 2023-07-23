class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        n1,n2=int(num1),int(num2)
        return str(n1+n2)

