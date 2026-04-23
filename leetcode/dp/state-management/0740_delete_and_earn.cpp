// LC 740. Delete and Earn | Medium (State Management DP)
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> earn(mx+1, 0);
        for (int n : nums) earn[n] += n;
        int p2 = 0, p1 = 0;
        for (int i = 0; i <= mx; i++) { int t = p1; p1 = max(p1, p2+earn[i]); p2 = t; }
        return p1;
    }
};
