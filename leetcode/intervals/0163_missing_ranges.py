# Track previous number and generate missing gaps.
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        res = []
        prev = lower - 1

        for n in nums + [upper + 1]:
            if n - prev >= 2:
                res.append(self._range(prev + 1, n - 1))
            prev = n

        return res

    def _range(self, lo, hi):
        return str(lo) if lo == hi else f"{lo}->{hi}"
