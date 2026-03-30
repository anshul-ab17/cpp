// LC 695. Max Area of Island | Medium
#include <vector>
using namespace std;

class Solution {
    int dfs(vector<vector<int>>& g, int i, int j) {
        if (i < 0 || i >= g.size() || j < 0 || j >= g[0].size() || g[i][j] != 1) return 0;
        g[i][j] = 0;
        return 1 + dfs(g,i+1,j) + dfs(g,i-1,j) + dfs(g,i,j+1) + dfs(g,i,j-1);
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); i++)
            for (int j = 0; j < grid[0].size(); j++) res = max(res, dfs(grid, i, j));
        return res;
    }
};
