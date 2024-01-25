class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapping = {"color": 1, "type": 0, "name": 2}
        idx = mapping[ruleKey]
        c = 0
        for item in items:
            if item[idx] == ruleValue:
                c += 1
        return c

