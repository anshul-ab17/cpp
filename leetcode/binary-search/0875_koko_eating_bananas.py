import math

class Solution:
    def minEatingSpeed(self, piles, h):

        def can_finish(speed):
            hours = sum(math.ceil(p / speed) for p in piles)
            return hours <= h

        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2

            if can_finish(m):
                r = m
            else:
                l = m + 1

        return l
