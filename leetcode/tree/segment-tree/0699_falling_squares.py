# Segment Tree with Coordinate Compression.
class Solution:
    def fallingSquares(self, positions):
        intervals = []
        res = []
        best = 0

        for left, size in positions:
            right = left + size
            base = 0
            for l, r, h in intervals:
                if l < right and left < r:
                    base = max(base, h)
            height = base + size
            intervals.append((left, right, height))
            best = max(best, height)
            res.append(best)

        return res
