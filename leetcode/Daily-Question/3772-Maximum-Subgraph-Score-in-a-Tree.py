import sys
sys.setrecursionlimit(300000)

class Solution:
    def maxSubgraphScore(self, n: int, edges: list[list[int]], good: list[int]) -> list[int]:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dp = [1 if good[i] else -1 for i in range(n)]

        def dfs1(node, parent):
            for nei in adj[node]:
                if nei != parent:
                    dfs1(nei, node)
                    if dp[nei] > 0:
                        dp[node] += dp[nei]

        dfs1(0, -1)

        ans = [0] * n

        def dfs2(node, parent, above):
            curr = dp[node] + max(0, above)
            ans[node] = curr

            for nei in adj[node]:
                if nei != parent:
                    rem = curr - dp[nei] if dp[nei] > 0 else curr
                    dfs2(nei, node, rem)

        dfs2(0, -1, 0)

        return ans
