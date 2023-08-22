class Solution:
    def convertToTitle(self, n: int) -> str:
        if n<27:
            return chr(ord('A')+(n-1)%26)
        c=""
        while n>0:
            if n%26==0:
                c+=chr(ord('A')+25)
                n-=1
            else:
                c+=chr(ord('A')+n%26-1)
            n//=26
        return c[::-1]
