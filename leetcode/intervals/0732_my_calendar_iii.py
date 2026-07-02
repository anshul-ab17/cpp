# Sweep Line using a sorted delta map (stdlib only).
class MyCalendarThree:
    def __init__(self):
        self.diff = {}
        self.best = 0

    def book(self, start, end):
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1

        cur = 0
        for point in sorted(self.diff):
            cur += self.diff[point]
            self.best = max(self.best, cur)

        return self.best
