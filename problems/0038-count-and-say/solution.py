class Solution:
    def countAndSay(self, n: int) -> str:
        import re

        currSeq = '1'
        pattern = r'((.)\2*)'

        for i in range(n-1):
            nextSeq = []
            for g1, g2 in re.findall(pattern, currSeq):
                # append the pair of <count, digit>
                nextSeq.append(str(len(g1)))
                nextSeq.append(g2)
            # prepare for the next iteration
            currSeq = ''.join(nextSeq)

        return currSeq
