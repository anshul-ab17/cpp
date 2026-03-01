# LC 307. Range Sum Query - Mutable | Medium (Fenwick Tree / BIT)
class NumArray:
    def __init__(self, nums):
        self.n = len(nums); self.nums = [0]*self.n; self.tree = [0]*(self.n+1)
        for i, v in enumerate(nums): self.update(i, v)
    def update(self, i, val):
        diff = val - self.nums[i]; self.nums[i] = val; i += 1
        while i <= self.n: self.tree[i] += diff; i += i & (-i)
    def _prefix(self, i):
        s = 0; i += 1
        while i > 0: s += self.tree[i]; i -= i & (-i)
        return s
    def sumRange(self, left, right):
        return self._prefix(right) - (self._prefix(left-1) if left > 0 else 0)
