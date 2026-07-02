# Fenwick Tree + Coordinate Compression.
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
    def countSmaller(self, nums):
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        fenwick = Fenwick(len(sorted_unique))
        res = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            r = rank[nums[i]]
            res[i] = fenwick.query(r - 1)
            fenwick.update(r)

        return res
