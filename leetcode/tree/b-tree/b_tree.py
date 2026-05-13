# B-Tree (order 3) - simplified insert
class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []; self.children = []; self.leaf = leaf

class BTree:
    def __init__(self, t=2):
        self.root = BTreeNode(); self.t = t
    def insert(self, k):
        r = self.root
        if len(r.keys) == 2*self.t - 1:
            s = BTreeNode(False); s.children.append(self.root)
            self._split(s, 0); self.root = s
        self._insert_non_full(self.root, k)
    def _split(self, parent, i):
        t = self.t; y = parent.children[i]; z = BTreeNode(y.leaf)
        parent.keys.insert(i, y.keys[t-1])
        parent.children.insert(i+1, z)
        z.keys = y.keys[t:]; y.keys = y.keys[:t-1]
        if not y.leaf: z.children = y.children[t:]; y.children = y.children[:t]
    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(k); x.keys.sort()
        else:
            while i >= 0 and k < x.keys[i]: i -= 1
            i += 1
            if len(x.children[i].keys) == 2*self.t - 1:
                self._split(x, i)
                if k > x.keys[i]: i += 1
            self._insert_non_full(x.children[i], k)

if __name__ == "__main__":
    bt = BTree(2)
    for k in [10,20,5,6,12,30,7,17]: bt.insert(k)
    print("B-Tree OK, root keys:", bt.root.keys)
