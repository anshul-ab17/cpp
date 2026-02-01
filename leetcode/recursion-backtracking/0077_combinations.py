class Solution:
    def combine(self, n, k):
        ans = []
        def dfs(start, cur):
            if len(cur) == k:
                ans.append(cur[:]); return
            for i in range(start, n+1):
                cur.append(i)
                dfs(i+1, cur)
                cur.pop()
        dfs(1, [])
        return ans
