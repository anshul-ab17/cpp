class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()

        def dfs(node):
            if node == destination:
                return True

            seen.add(node)

            for nei in graph[node]:
                if nei not in seen and dfs(nei):
                    return True

            return False

        return dfs(source)
