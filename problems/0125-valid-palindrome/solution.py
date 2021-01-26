class Solution:
    def isPalindrome(self, s: str) -> bool:
        extracted = "".join(re.findall("[a-zA-Z0-9]+", s.lower()))
        return extracted == extracted[::-1]
