# LC 94. Binary Tree Inorder Traversal | Easy
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def inorderTraversal_rec(self, root):
        if not root: return []
        return self.inorderTraversal_rec(root.left) + [root.val] + self.inorderTraversal_rec(root.right)

    def inorderTraversal(self, root):
        res, stack, curr = [], [], root
        while curr or stack:
            while curr: stack.append(curr); curr = curr.left
            curr = stack.pop(); res.append(curr.val); curr = curr.right
        return res
