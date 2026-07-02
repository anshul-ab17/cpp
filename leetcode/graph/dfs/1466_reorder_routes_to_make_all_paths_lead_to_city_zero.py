# DFS + Directed edges trick.
class Solution:
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        visited = [False] * n
        count = 0

        def dfs(node):
            nonlocal count
            visited[node] = True
            for nxt, cost in graph[node]:
                if not visited[nxt]:
                    count += cost
                    dfs(nxt)

        dfs(0)
        return count
