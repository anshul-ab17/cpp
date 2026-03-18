# AVL Tree Implementation
class Node:
    def __init__(self, key):
        self.key = key; self.left = self.right = None; self.height = 1

class AVLTree:
    def h(self, n): return n.height if n else 0
    def bal(self, n): return self.h(n.left) - self.h(n.right) if n else 0
    def rotR(self, y):
        x = y.left; y.left = x.right; x.right = y
        y.height = 1 + max(self.h(y.left), self.h(y.right))
        x.height = 1 + max(self.h(x.left), self.h(x.right)); return x
    def rotL(self, x):
        y = x.right; x.right = y.left; y.left = x
        x.height = 1 + max(self.h(x.left), self.h(x.right))
        y.height = 1 + max(self.h(y.left), self.h(y.right)); return y
    def insert(self, node, key):
        if not node: return Node(key)
        if key < node.key: node.left = self.insert(node.left, key)
        elif key > node.key: node.right = self.insert(node.right, key)
        else: return node
        node.height = 1 + max(self.h(node.left), self.h(node.right))
        b = self.bal(node)
        if b > 1 and key < node.left.key: return self.rotR(node)
        if b < -1 and key > node.right.key: return self.rotL(node)
        if b > 1 and key > node.left.key: node.left = self.rotL(node.left); return self.rotR(node)
        if b < -1 and key < node.right.key: node.right = self.rotR(node.right); return self.rotL(node)
        return node

if __name__ == "__main__":
    avl = AVLTree(); root = None
    for k in [10,20,30,40,50,25]: root = avl.insert(root, k)
    print("AVL OK")
