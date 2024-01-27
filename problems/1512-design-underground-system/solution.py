class UndergroundSystem:

    def __init__(self):
        self.inside_train = {}
        self.stamps = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inside_train[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if not id in self.inside_train:
            return
        start_station, start_t = self.inside_train[id]
        self.stamps[(start_station, stationName)].append(t - start_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travels = self.stamps[(startStation, endStation)]
        return sum(travels) / len(travels)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
