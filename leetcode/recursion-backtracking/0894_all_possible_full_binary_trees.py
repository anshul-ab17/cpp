# Recursively build all left/right subtree combinations.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return []

        memo = {1: [TreeNode(0)]}

        def build(n):
            if n in memo:
                return memo[n]
            res = []
            for left in range(1, n, 2):
                right = n - 1 - left
                for l in build(left):
                    for r in build(right):
                        res.append(TreeNode(0, l, r))
            memo[n] = res
            return res

        return build(n)
