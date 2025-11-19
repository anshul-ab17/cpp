class Solution:
    def buildTree(self, preorder, inorder):
        pos = {v:i for i,v in enumerate(inorder)}
        i = 0
        def dfs(l, r):
            nonlocal i
            if l > r: return None
            root = TreeNode(preorder[i]); i += 1
            mid = pos[root.val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)
