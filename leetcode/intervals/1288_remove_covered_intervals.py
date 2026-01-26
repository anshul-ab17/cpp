class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count, end = 0, 0

        for _, e in intervals:
            if e > end:
                count += 1
                end = e

        return count
