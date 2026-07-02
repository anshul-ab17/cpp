# Fenwick Tree frequency counts.
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
    def createSortedArray(self, instructions):
        MOD = 10 ** 9 + 7
        max_val = max(instructions)
        fenwick = Fenwick(max_val + 1)
        cost = 0

        for i, num in enumerate(instructions):
            less = fenwick.query(num - 1)
            greater = i - fenwick.query(num)
            cost += min(less, greater)
            fenwick.update(num)

        return cost % MOD
