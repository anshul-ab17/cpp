# Union rows and columns.
class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

class Solution:
    def removeStones(self, stones):
        dsu = DSU()
        for r, c in stones:
            dsu.union(('r', r), ('c', c))

        roots = {dsu.find(('r', r)) for r, c in stones}
        return len(stones) - len(roots)
