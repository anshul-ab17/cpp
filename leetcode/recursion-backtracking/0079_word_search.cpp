// LC 79. Word Search | Medium
#include <vector>
#include <string>
using namespace std;

class Solution {
    int m, n;
    bool dfs(vector<vector<char>>& b, string& w, int i, int j, int k) {
        if (k == w.size()) return true;
        if (i < 0 || i >= m || j < 0 || j >= n || b[i][j] != w[k]) return false;
        char tmp = b[i][j]; b[i][j] = '#';
        int d[] = {0,1,0,-1,0};
        for (int x = 0; x < 4; x++) if (dfs(b, w, i+d[x], j+d[x+1], k+1)) return true;
        b[i][j] = tmp; return false;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size(); n = board[0].size();
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++)
            if (dfs(board, word, i, j, 0)) return true;
        return false;
    }
};
