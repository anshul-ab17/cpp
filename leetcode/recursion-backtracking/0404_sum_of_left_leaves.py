class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        ans = 0
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val

        return ans + self.sumOfLeftLeaves(root.left) +                self.sumOfLeftLeaves(root.right)
