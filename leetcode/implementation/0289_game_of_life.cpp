// LC 289. Game of Life | Medium
#include <vector>
using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                int live = 0;
                for (int di = -1; di <= 1; di++)
                    for (int dj = -1; dj <= 1; dj++) {
                        if (!di && !dj) continue;
                        int ni = i+di, nj = j+dj;
                        if (ni >= 0 && ni < m && nj >= 0 && nj < n && (board[ni][nj] & 1)) live++;
                    }
                if ((board[i][j] & 1) && (live == 2 || live == 3)) board[i][j] |= 2;
                else if (!(board[i][j] & 1) && live == 3) board[i][j] |= 2;
            }
        for (auto& row : board) for (auto& c : row) c >>= 1;
    }
};
