# Reverse graph + Topological Sort (color-based DFS also works).
class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        color = [0] * n  # 0=unvisited, 1=visiting, 2=safe

        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if dfs(i)]
