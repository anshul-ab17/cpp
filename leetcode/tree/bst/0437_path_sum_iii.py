from collections import defaultdict
class Solution:
    def pathSum(self, root, target):
        pref = defaultdict(int); pref[0] = 1
        ans = 0
        def dfs(node, cur):
            nonlocal ans
            if not node: return
            cur += node.val
            ans += pref[cur-target]
            pref[cur] += 1
            dfs(node.left, cur); dfs(node.right, cur)
            pref[cur] -= 1
        dfs(root, 0)
        return ans
