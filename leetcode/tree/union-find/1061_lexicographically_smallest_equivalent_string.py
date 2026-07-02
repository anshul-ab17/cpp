# Union chars and always attach larger root to smaller root.
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
        if ra == rb:
            return
        if ra < rb:
            self.parent[rb] = ra
        else:
            self.parent[ra] = rb

class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        dsu = DSU(26)
        for a, b in zip(s1, s2):
            dsu.union(ord(a) - 97, ord(b) - 97)

        return "".join(chr(dsu.find(ord(ch) - 97) + 97) for ch in baseStr)
