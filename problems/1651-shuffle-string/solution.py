class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for char, idx in zip(s, indices):
            result[idx] = char
        return "".join(result)

