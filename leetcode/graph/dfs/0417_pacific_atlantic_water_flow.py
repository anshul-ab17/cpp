# LC 417. Pacific Atlantic Water Flow | Medium
class Solution:
    def pacificAtlantic(self, heights):
        if not heights: return []
        m, n = len(heights), len(heights[0]); pac, atl = set(), set()
        def dfs(i, j, visited, prev_h):
            if i < 0 or i >= m or j < 0 or j >= n: return
            if (i,j) in visited or heights[i][j] < prev_h: return
            visited.add((i,j))
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i+di, j+dj, visited, heights[i][j])
        for j in range(n): dfs(0, j, pac, 0); dfs(m-1, j, atl, 0)
        for i in range(m): dfs(i, 0, pac, 0); dfs(i, n-1, atl, 0)
        return list(pac & atl)
