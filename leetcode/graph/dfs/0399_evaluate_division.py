# Build weighted graph + DFS.
from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for nxt, val in graph[src].items():
                if nxt in visited:
                    continue
                res = dfs(nxt, dst, visited)
                if res != -1.0:
                    return val * res
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
