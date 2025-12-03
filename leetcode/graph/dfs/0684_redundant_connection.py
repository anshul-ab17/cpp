class DSU:
    def __init__(self,n):
        self.p=list(range(n+1))

    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def union(self,a,b):
        pa,pb=self.find(a),self.find(b)
        if pa==pb: return False
        self.p[pa]=pb
        return True

class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges))
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
