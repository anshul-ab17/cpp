// LC 994. Rotting Oranges | Medium
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), fresh = 0, time = 0;
        queue<pair<int,int>> q;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.push({i,j});
                else if (grid[i][j] == 1) fresh++;
            }
        int d[] = {0,1,0,-1,0};
        while (!q.empty() && fresh) {
            time++; int sz = q.size();
            while (sz--) {
                auto [i,j] = q.front(); q.pop();
                for (int x = 0; x < 4; x++) {
                    int ni = i+d[x], nj = j+d[x+1];
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1) {
                        grid[ni][nj] = 2; fresh--; q.push({ni,nj});
                    }
                }
            }
        }
        return fresh == 0 ? time : -1;
    }
};
