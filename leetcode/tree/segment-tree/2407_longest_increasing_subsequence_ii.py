# Segment Tree range maximum query.
class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, idx, val, node=1, lo=0, hi=None):
        if hi is None:
            hi = self.n - 1
        if lo == hi:
            self.tree[node] = max(self.tree[node], val)
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self.update(idx, val, node * 2, lo, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, hi)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, l, r, node=1, lo=0, hi=None):
        if hi is None:
            hi = self.n - 1
        if r < lo or hi < l or l > r:
            return 0
        if l <= lo and hi <= r:
            return self.tree[node]
        mid = (lo + hi) // 2
        return max(
            self.query(l, r, node * 2, lo, mid),
            self.query(l, r, node * 2 + 1, mid + 1, hi),
        )

class Solution:
    def lengthOfLIS(self, nums, k):
        max_val = max(nums)
        tree = SegTree(max_val + 1)
        best = 0

        for num in nums:
            lo = max(1, num - k)
            best_prev = tree.query(lo, num - 1)
            cur = best_prev + 1
            tree.update(num, cur)
            best = max(best, cur)

        return best
