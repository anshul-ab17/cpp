// LC 494. Target Sum | Medium (Knapsack variant)
#include <vector>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = 0; for (int n : nums) total += n;
        if ((total+target)%2 || abs(target) > total) return 0;
        int s = (total+target)/2;
        vector<int> dp(s+1, 0); dp[0] = 1;
        for (int n : nums) for (int j = s; j >= n; j--) dp[j] += dp[j-n];
        return dp[s];
    }
};
