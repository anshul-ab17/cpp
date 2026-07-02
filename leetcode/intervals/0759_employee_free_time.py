# Merge all intervals and find gaps.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule):
        intervals = sorted((iv for emp in schedule for iv in emp), key=lambda iv: iv.start)
        res = []
        end = intervals[0].end

        for iv in intervals[1:]:
            if iv.start > end:
                res.append(Interval(end, iv.start))
                end = iv.end
            else:
                end = max(end, iv.end)

        return res
