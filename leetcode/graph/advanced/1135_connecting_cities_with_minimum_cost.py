# Kruskal MST + DSU.
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        return True

class Solution:
    def minimumCost(self, n, connections):
        dsu = DSU(n)
        connections.sort(key=lambda c: c[2])
        total = 0
        edges = 0

        for u, v, cost in connections:
            if dsu.union(u, v):
                total += cost
                edges += 1

        return total if edges == n - 1 else -1
