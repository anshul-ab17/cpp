# Fenwick Tree simulate removals.
class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        while i <= len(self.tree) - 1:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total

class Solution:
    def countOperationsToEmptyArray(self, nums):
        n = len(nums)
        order = sorted(range(n), key=lambda i: nums[i])
        fenwick = Fenwick(n)
        for i in range(1, n + 1):
            fenwick.update(i, 1)

        ops = 0
        prev = 0  # 1-indexed position of previously removed element (0 = none yet)

        for idx in order:
            pos = idx + 1
            if pos > prev:
                ops += fenwick.query(pos) - fenwick.query(prev)
            else:
                ops += (fenwick.query(n) - fenwick.query(prev)) + fenwick.query(pos)
            fenwick.update(pos, -1)
            prev = pos

        return ops
