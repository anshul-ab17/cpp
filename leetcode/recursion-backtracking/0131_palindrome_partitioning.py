class Solution:
    def partition(self, s):
        ans = []
        def dfs(i, cur):
            if i == len(s):
                ans.append(cur[:]); return
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    cur.append(sub)
                    dfs(j+1, cur)
                    cur.pop()
        dfs(0, [])
        return ans
