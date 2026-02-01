class Solution:
    def generateTrees(self, n):
        def build(l, r):
            if l > r:
                return [None]

            ans = []
            for root in range(l, r + 1):
                for left in build(l, root - 1):
                    for right in build(root + 1, r):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        ans.append(node)

            return ans

        return build(1, n)
