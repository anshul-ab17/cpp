# Brute force geometry.
class Solution:
    def countPoints(self, points, queries):
        res = []
        for x, y, r in queries:
            count = 0
            for px, py in points:
                if (px - x) ** 2 + (py - y) ** 2 <= r * r:
                    count += 1
            res.append(count)
        return res
