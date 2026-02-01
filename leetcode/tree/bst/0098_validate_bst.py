# LC 98. Validate Binary Search Tree | Medium
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def isValidBST(self, root, lo=float('-inf'), hi=float('inf')):
        if not root: return True
        if root.val <= lo or root.val >= hi: return False
        return self.isValidBST(root.left, lo, root.val) and self.isValidBST(root.right, root.val, hi)
