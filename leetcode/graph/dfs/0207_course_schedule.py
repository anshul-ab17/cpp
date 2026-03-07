# LC 207. Course Schedule | Medium
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: graph[a].append(b)
        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done
        def dfs(node):
            if state[node] == 1: return False
            if state[node] == 2: return True
            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei): return False
            state[node] = 2; return True
        return all(dfs(i) for i in range(numCourses))
