class Solution:
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[1])
        arrows, end = 1, points[0][1]
        for s,e in points[1:]:
            if s > end:
                arrows += 1
                end = e
        return arrows
