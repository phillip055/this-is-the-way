class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """

        c = Counter(tasks)
        rounds = 0
        for _, v in enumerate(c):
            v = c[v]
            if v < 2: return -1
            
            if v >= 3:
                remainder = v % 3
                floor = v // 3
                if remainder != 0:
                    floor += 1
                rounds += floor
            elif v >= 2:
                remainder = v % 2
                floor = v // 2
                if remainder != 0:
                    floor += 1
                rounds += floor
        return rounds

