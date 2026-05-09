// LC 1091. Shortest Path in Binary Matrix | Medium
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();
        if (grid[0][0] || grid[n-1][n-1]) return -1;
        queue<tuple<int,int,int>> q; q.push({0,0,1}); grid[0][0] = 1;
        while (!q.empty()) {
            auto [i,j,d] = q.front(); q.pop();
            if (i == n-1 && j == n-1) return d;
            for (int di = -1; di <= 1; di++)
                for (int dj = -1; dj <= 1; dj++) {
                    int ni = i+di, nj = j+dj;
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n && !grid[ni][nj]) {
                        grid[ni][nj] = 1; q.push({ni,nj,d+1});
                    }
                }
        }
        return -1;
    }
};
