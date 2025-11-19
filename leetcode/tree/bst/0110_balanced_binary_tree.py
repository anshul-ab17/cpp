class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            if l == -1 or r == -1 or abs(l-r) > 1: return -1
            return 1 + max(l, r)
        return dfs(root) != -1
