class Solution:
    def diameterOfBinaryTree(self, root):
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)
        dfs(root)
        return ans
