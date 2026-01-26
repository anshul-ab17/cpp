class MyCalendar:
    def __init__(self):
        self.books = []

    def book(self, start, end):
        for s, e in self.books:
            if max(s, start) < min(e, end):
                return False
        self.books.append((start, end))
        return True
