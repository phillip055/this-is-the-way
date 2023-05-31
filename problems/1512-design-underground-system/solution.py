class UndergroundSystem:
    def __init__(self):
        self.active_ids = {}
        self.summary = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.active_ids:
            return None
        self.active_ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start_time = self.active_ids[id]
        time_taken = t - start_time
        del self.active_ids[id]
        if (startStation, stationName) in self.summary:
            self.summary[(startStation, stationName)]["total"] += time_taken
            self.summary[(startStation, stationName)]["count"] += 1
        else:
            self.summary[(startStation, stationName)] = {}
            self.summary[(startStation, stationName)]["total"] = time_taken
            self.summary[(startStation, stationName)]["count"] = 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.summary[(startStation, endStation)]["total"] / self.summary[(startStation, endStation)]["count"]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

