# Fenwick / Merge Sort + Prefix Sum.
from bisect import bisect_left, bisect_right, insort

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = 0
        sums = [0]
        count = 0

        for x in nums:
            prefix += x
            lo = bisect_left(sums, prefix - upper)
            hi = bisect_right(sums, prefix - lower)
            count += hi - lo
            insort(sums, prefix)

        return count
