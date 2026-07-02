# HashMaps for check-in and route stats.
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.stats = defaultdict(lambda: [0, 0])

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        start_station, start_t = self.checkins.pop(id)
        key = (start_station, stationName)
        self.stats[key][0] += t - start_t
        self.stats[key][1] += 1

    def getAverageTime(self, startStation, endStation):
        total, count = self.stats[(startStation, endStation)]
        return total / count
