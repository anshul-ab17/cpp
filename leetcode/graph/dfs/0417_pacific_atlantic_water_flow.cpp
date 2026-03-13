// LC 417. Pacific Atlantic Water Flow | Medium
#include <vector>
using namespace std;

class Solution {
    int m, n;
    void dfs(vector<vector<int>>& h, vector<vector<bool>>& vis, int i, int j) {
        vis[i][j] = true;
        int d[] = {0,1,0,-1,0};
        for (int x = 0; x < 4; x++) {
            int ni = i+d[x], nj = j+d[x+1];
            if (ni >= 0 && ni < m && nj >= 0 && nj < n && !vis[ni][nj] && h[ni][nj] >= h[i][j])
                dfs(h, vis, ni, nj);
        }
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size(); n = heights[0].size();
        vector<vector<bool>> pac(m, vector<bool>(n)), atl(m, vector<bool>(n));
        for (int j = 0; j < n; j++) { dfs(heights, pac, 0, j); dfs(heights, atl, m-1, j); }
        for (int i = 0; i < m; i++) { dfs(heights, pac, i, 0); dfs(heights, atl, i, n-1); }
        vector<vector<int>> res;
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)
            if (pac[i][j] && atl[i][j]) res.push_back({i, j});
        return res;
    }
};
