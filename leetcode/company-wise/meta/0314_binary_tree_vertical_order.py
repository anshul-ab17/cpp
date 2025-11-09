# LC 314. Binary Tree Vertical Order Traversal | Medium | Meta
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def verticalOrder(self, root):
        if not root: return []
        cols = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, col = q.popleft()
            cols[col].append(node.val)
            if node.left: q.append((node.left, col-1))
            if node.right: q.append((node.right, col+1))
        return [cols[k] for k in sorted(cols)]
