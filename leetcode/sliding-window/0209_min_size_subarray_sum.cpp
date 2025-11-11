// LC 209. Minimum Size Subarray Sum | Medium
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, s = 0, res = INT_MAX;
        for (int r = 0; r < nums.size(); r++) {
            s += nums[r];
            while (s >= target) { res = min(res, r - l + 1); s -= nums[l++]; }
        }
        return res == INT_MAX ? 0 : res;
    }
};
