# Red-Black Tree - Simplified Insert Only
RED, BLACK = True, False

class Node:
    def __init__(self, key, color=RED):
        self.key = key; self.color = color; self.left = self.right = self.parent = None

class RBTree:
    def __init__(self): self.nil = Node(0, BLACK); self.root = self.nil

    def insert(self, key):
        node = Node(key); node.left = node.right = node.parent = self.nil
        parent = self.nil; curr = self.root
        while curr != self.nil:
            parent = curr
            curr = curr.left if key < curr.key else curr.right
        node.parent = parent
        if parent == self.nil: self.root = node
        elif key < parent.key: parent.left = node
        else: parent.right = node
        self._fix_insert(node)

    def _fix_insert(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = y.color = BLACK; z.parent.parent.color = RED; z = z.parent.parent
                else:
                    if z == z.parent.right: z = z.parent; self._left_rotate(z)
                    z.parent.color = BLACK; z.parent.parent.color = RED; self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = y.color = BLACK; z.parent.parent.color = RED; z = z.parent.parent
                else:
                    if z == z.parent.left: z = z.parent; self._right_rotate(z)
                    z.parent.color = BLACK; z.parent.parent.color = RED; self._left_rotate(z.parent.parent)
        self.root.color = BLACK

    def _left_rotate(self, x):
        y = x.right; x.right = y.left
        if y.left != self.nil: y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil: self.root = y
        elif x == x.parent.left: x.parent.left = y
        else: x.parent.right = y
        y.left = x; x.parent = y

    def _right_rotate(self, y):
        x = y.left; y.left = x.right
        if x.right != self.nil: x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil: self.root = x
        elif y == y.parent.right: y.parent.right = x
        else: y.parent.left = x
        x.right = y; y.parent = x

if __name__ == "__main__":
    t = RBTree()
    for k in [7,3,18,10,22,8,11,26]: t.insert(k)
    print("RB Tree OK")
