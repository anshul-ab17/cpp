from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key, value, timestamp):
        self.mp[key].append((timestamp, value))

    def get(self, key, timestamp):
        arr = self.mp[key]
        i = bisect_right(arr, (timestamp, chr(127))) - 1
        return arr[i][1] if i >= 0 else ""
