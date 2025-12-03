class Solution:
    def isBipartite(self, graph):
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c

            color[node] = c

            for nei in graph[node]:
                if not dfs(nei, -c):
                    return False
            return True

        return all(dfs(i,1) for i in range(len(graph)) if i not in color)
