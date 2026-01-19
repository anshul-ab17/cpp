// LC 46. Permutations | Medium
#include <vector>
using namespace std;

class Solution {
    void bt(vector<int>& nums, int start, vector<vector<int>>& res) {
        if (start == nums.size()) { res.push_back(nums); return; }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]); bt(nums, start+1, res); swap(nums[start], nums[i]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res; bt(nums, 0, res); return res;
    }
};
