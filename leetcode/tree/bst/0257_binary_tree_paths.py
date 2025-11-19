class Solution:
    def binaryTreePaths(self, root):
        ans = []
        def dfs(node, path):
            if not node: return
            if not node.left and not node.right:
                ans.append(path + str(node.val)); return
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')
        dfs(root, '')
        return ans
