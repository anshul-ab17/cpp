# Fenwick Tree + Coordinate Compression.
from bisect import bisect_right

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta=1):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        d = [nums1[i] - nums2[i] for i in range(n)]

        sorted_unique = sorted(set(d))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        fenwick = Fenwick(len(sorted_unique))

        count = 0
        for i in range(n):
            # need d[j] <= d[i] + diff for j < i
            limit = d[i] + diff
            idx = bisect_right(sorted_unique, limit)
            count += fenwick.query(idx)
            fenwick.update(rank[d[i]])

        return count
