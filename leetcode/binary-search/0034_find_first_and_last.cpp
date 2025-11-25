// LC 34. Find First and Last Position | Medium
#include <vector>
using namespace std;

class Solution {
    int find(vector<int>& nums, int target, bool leftBias) {
        int l = 0, r = nums.size() - 1, idx = -1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) { idx = m; if (leftBias) r = m - 1; else l = m + 1; }
            else if (nums[m] < target) l = m + 1; else r = m - 1;
        }
        return idx;
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return {find(nums, target, true), find(nums, target, false)};
    }
};
