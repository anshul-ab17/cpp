// LC 130. Surrounded Regions | Medium
#include <vector>
using namespace std;

class Solution {
    int m, n;
    void dfs(vector<vector<char>>& b, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || b[i][j] != 'O') return;
        b[i][j] = 'S'; dfs(b,i+1,j); dfs(b,i-1,j); dfs(b,i,j+1); dfs(b,i,j-1);
    }
public:
    void solve(vector<vector<char>>& board) {
        m = board.size(); n = board[0].size();
        for (int i = 0; i < m; i++) { dfs(board,i,0); dfs(board,i,n-1); }
        for (int j = 0; j < n; j++) { dfs(board,0,j); dfs(board,m-1,j); }
        for (auto& row : board) for (auto& c : row) c = c == 'S' ? 'O' : 'X';
    }
};
