// LC 221. Maximal Square | Medium
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), mx = 0;
        vector<int> dp(n+1, 0);
        for (int i = 0; i < m; i++) {
            vector<int> ndp(n+1, 0);
            for (int j = 1; j <= n; j++)
                if (matrix[i][j-1] == '1') { ndp[j] = min({dp[j], dp[j-1], ndp[j-1]})+1; mx = max(mx, ndp[j]); }
            dp = ndp;
        }
        return mx*mx;
    }
};
