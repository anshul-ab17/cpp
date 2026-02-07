// LC 51. N-Queens | Hard
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
    unordered_set<int> cols, diag, anti;
    void bt(int row, int n, vector<string>& board, vector<vector<string>>& res) {
        if (row == n) { res.push_back(board); return; }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || diag.count(row-col) || anti.count(row+col)) continue;
            cols.insert(col); diag.insert(row-col); anti.insert(row+col);
            board[row][col] = 'Q'; bt(row+1, n, board, res); board[row][col] = '.';
            cols.erase(col); diag.erase(row-col); anti.erase(row+col);
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res; vector<string> board(n, string(n, '.'));
        bt(0, n, board, res); return res;
    }
};
