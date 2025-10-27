// LC 11. Container With Most Water | Medium
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& h) {
        int l = 0, r = h.size() - 1, res = 0;
        while (l < r) {
            res = max(res, min(h[l], h[r]) * (r - l));
            if (h[l] < h[r]) l++; else r--;
        }
        return res;
    }
};
