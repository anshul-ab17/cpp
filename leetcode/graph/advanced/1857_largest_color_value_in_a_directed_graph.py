# Topological Sort + DP.
from collections import deque, defaultdict

class Solution:
    def largestPathValue(self, colors, edges):
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        count = [[0] * 26 for _ in range(n)]
        queue = deque(i for i in range(n) if indegree[i] == 0)
        visited = 0
        best = 0

        while queue:
            node = queue.popleft()
            visited += 1
            count[node][ord(colors[node]) - 97] += 1
            best = max(best, count[node][ord(colors[node]) - 97])
            for nxt in graph[node]:
                for c in range(26):
                    count[nxt][c] = max(count[nxt][c], count[node][c])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return best if visited == n else -1
