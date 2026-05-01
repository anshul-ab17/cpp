# LC 337. House Robber III | Medium (DP on Tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def rob(self, root):
        def dfs(node):
            if not node: return (0, 0)
            l = dfs(node.left); r = dfs(node.right)
            rob_it = node.val + l[1] + r[1]
            skip_it = max(l) + max(r)
            return (rob_it, skip_it)
        return max(dfs(root))
