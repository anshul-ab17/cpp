# Union by common factors.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.size[ra] < self.size[rb]:
                ra, rb = rb, ra
            self.parent[rb] = ra
            self.size[ra] += self.size[rb]

class Solution:
    def largestComponentSize(self, nums):
        max_val = max(nums)
        dsu = DSU(max_val + 1)

        for num in nums:
            factor = 2
            n = num
            while factor * factor <= n:
                if n % factor == 0:
                    dsu.union(num, factor)
                    while n % factor == 0:
                        n //= factor
                factor += 1
            if n > 1:
                dsu.union(num, n)

        count = {}
        best = 0
        for num in nums:
            root = dsu.find(num)
            count[root] = count.get(root, 0) + 1
            best = max(best, count[root])

        return best
