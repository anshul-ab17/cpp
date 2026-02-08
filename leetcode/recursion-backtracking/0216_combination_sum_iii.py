class Solution:
    def combinationSum3(self, k, n):
        ans = []
        def dfs(start, cur, total):
            if len(cur) == k and total == n:
                ans.append(cur[:]); return
            if len(cur) >= k or total > n: return
            for i in range(start, 10):
                cur.append(i)
                dfs(i+1, cur, total+i)
                cur.pop()
        dfs(1, [], 0)
        return ans
