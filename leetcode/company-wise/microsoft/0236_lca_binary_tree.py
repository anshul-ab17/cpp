# LC 236. Lowest Common Ancestor of a Binary Tree | Medium | Microsoft, Meta
class TreeNode:
    def __init__(self, x): self.val = x; self.left = self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left or right
