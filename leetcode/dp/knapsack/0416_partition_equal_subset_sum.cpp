// LC 416. Partition Equal Subset Sum | Medium (0/1 Knapsack)
#include <vector>
using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int total = 0; for (int n : nums) total += n;
        if (total % 2) return false;
        int target = total / 2;
        vector<bool> dp(target+1, false); dp[0] = true;
        for (int n : nums)
            for (int j = target; j >= n; j--) dp[j] = dp[j] || dp[j-n];
        return dp[target];
    }
};
