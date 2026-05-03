# LC 124. Binary Tree Maximum Path Sum | Hard (DP on Tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')
        def dfs(node):
            if not node: return 0
            l = max(dfs(node.left), 0); r = max(dfs(node.right), 0)
            self.ans = max(self.ans, node.val + l + r)
            return node.val + max(l, r)
        dfs(root); return self.ans
