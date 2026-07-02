# Reflection around middle line.
class Solution:
    def isReflected(self, points):
        if not points:
            return True

        xs = [x for x, _ in points]
        min_x, max_x = min(xs), max(xs)
        total = min_x + max_x
        point_set = {(x, y) for x, y in points}

        for x, y in points:
            if (total - x, y) not in point_set:
                return False

        return True
