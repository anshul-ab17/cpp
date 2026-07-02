# Group indices using DSU.
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        dsu = DSU(n)
        for a, b in pairs:
            dsu.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[dsu.find(i)].append(i)

        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            for i, ch in zip(sorted(indices), chars):
                res[i] = ch

        return "".join(res)
