class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        device_floor = []
        for floor in bank:
            c = floor.count("1")
            if c:
                device_floor.append(c)
        if len(device_floor) <= 1:
            return 0
        _sum = 0
        for idx in range(1, len(device_floor)):
            _sum += device_floor[idx - 1] * device_floor[idx]
        return _sum

