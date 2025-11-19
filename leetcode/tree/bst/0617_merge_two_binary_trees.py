class Solution:
    def mergeTrees(self, a, b):
        if not a: return b
        if not b: return a
        a.val += b.val
        a.left = self.mergeTrees(a.left, b.left)
        a.right = self.mergeTrees(a.right, b.right)
        return a
