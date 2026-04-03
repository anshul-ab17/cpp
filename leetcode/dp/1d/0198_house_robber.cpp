// LC 198. House Robber | Medium
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int p2 = 0, p1 = 0;
        for (int n : nums) { int t = p1; p1 = max(p1, p2 + n); p2 = t; }
        return p1;
    }
};
