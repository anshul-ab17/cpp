// LC 1986. Minimum Number of Work Sessions | Medium (Bitmask DP)
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size(), total = 1 << n;
        vector<int> dp(total, n+1), ss(total, 0);
        dp[0] = 0;
        for (int mask = 1; mask < total; mask++)
            for (int i = 0; i < n; i++)
                if (mask & (1<<i)) { ss[mask] = ss[mask^(1<<i)] + tasks[i]; break; }
        for (int mask = 1; mask < total; mask++)
            for (int sub = mask; sub; sub = (sub-1)&mask)
                if (ss[sub] <= sessionTime) dp[mask] = min(dp[mask], dp[mask^sub]+1);
        return dp[total-1];
    }
};
