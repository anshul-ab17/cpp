# Maintain booked and overlapped intervals.
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        for s, e in self.overlaps:
            if start < e and s < end:
                return False

        for s, e in self.bookings:
            if start < e and s < end:
                self.overlaps.append((max(start, s), min(end, e)))

        self.bookings.append((start, end))
        return True
