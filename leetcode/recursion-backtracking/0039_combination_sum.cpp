// LC 39. Combination Sum | Medium
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    void bt(vector<int>& c, int start, int remain, vector<int>& path, vector<vector<int>>& res) {
        if (remain == 0) { res.push_back(path); return; }
        for (int i = start; i < c.size() && c[i] <= remain; i++) {
            path.push_back(c[i]); bt(c, i, remain-c[i], path, res); path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& c, int target) {
        sort(c.begin(), c.end()); vector<vector<int>> res; vector<int> path;
        bt(c, 0, target, path, res); return res;
    }
};
