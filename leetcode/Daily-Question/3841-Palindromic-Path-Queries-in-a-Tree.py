import sys
sys.setrecursionlimit(300000)

class Solution:
    def palindromicPathQueries(
        self,
        n: int,
        edges: list[list[int]],
        labels: str,
        queries: list[list[int]]
    ) -> list[bool]:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = 18
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        mask = [0] * n

        def dfs(node, parent, dep, cur_mask):
            depth[node] = dep

            cur_mask ^= 1 << (ord(labels[node]) - ord('a'))
            mask[node] = cur_mask

            up[node][0] = parent if parent != -1 else node

            for i in range(1, LOG):
                up[node][i] = up[up[node][i - 1]][i - 1]

            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node, dep + 1, cur_mask)

        dfs(0, -1, 0, 0)

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]

            if u == v:
                return u

            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]

            return up[u][0]

        ans = []

        for u, v in queries:
            p = lca(u, v)

            cur = (
                mask[u]
                ^ mask[v]
                ^ (1 << (ord(labels[p]) - ord('a')))
            )

            ans.append((cur & (cur - 1)) == 0)

        return ans
