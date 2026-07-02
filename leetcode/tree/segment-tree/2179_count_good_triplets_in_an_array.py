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
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        pos_in_2 = [0] * n
        for i, v in enumerate(nums2):
            pos_in_2[v] = i

        mapped = [pos_in_2[v] for v in nums1]

        left_smaller = [0] * n
        fenwick = Fenwick(n)
        for i in range(n):
            left_smaller[i] = fenwick.query(mapped[i])
            fenwick.update(mapped[i] + 1)

        right_greater = [0] * n
        fenwick2 = Fenwick(n)
        for i in range(n - 1, -1, -1):
            right_greater[i] = fenwick2.query(n) - fenwick2.query(mapped[i] + 1)
            fenwick2.update(mapped[i] + 1)

        return sum(left_smaller[i] * right_greater[i] for i in range(n))
