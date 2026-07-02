# Tarjan Algorithm (Bridges).
class Solution:
    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc = [-1] * n
        low = [0] * n
        timer = [0]
        bridges = []

        def dfs(node, parent):
            disc[node] = low[node] = timer[0]
            timer[0] += 1
            for nxt in graph[node]:
                if nxt == parent:
                    continue
                if disc[nxt] == -1:
                    dfs(nxt, node)
                    low[node] = min(low[node], low[nxt])
                    if low[nxt] > disc[node]:
                        bridges.append([node, nxt])
                else:
                    low[node] = min(low[node], disc[nxt])

        dfs(0, -1)
        return bridges
