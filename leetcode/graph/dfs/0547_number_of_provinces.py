class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        seen = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and j not in seen:
                    seen.add(j)
                    dfs(j)

        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        return ans
