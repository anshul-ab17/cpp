# LC 210. Course Schedule II | Medium (Topological Sort)
from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites: graph[b].append(a); indeg[a] += 1
        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            node = q.popleft(); order.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0: q.append(nei)
        return order if len(order) == numCourses else []
