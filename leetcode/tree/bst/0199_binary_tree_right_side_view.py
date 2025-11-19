from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root: return []
        q, ans = deque([root]), []
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0: ans.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return ans
