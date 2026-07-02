# Monotonic deque optimization.
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points, k):
        dq = deque()  # stores (y - x, x)
        best = float('-inf')

        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()
            if dq:
                best = max(best, x + y + dq[0][0])
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append((y - x, x))

        return best
