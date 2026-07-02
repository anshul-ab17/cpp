# Sort logs by time + DSU.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb
            self.count -= 1

class Solution:
    def earliestAcq(self, logs, n):
        logs.sort(key=lambda x: x[0])
        dsu = DSU(n)

        for t, a, b in logs:
            dsu.union(a, b)
            if dsu.count == 1:
                return t

        return -1
