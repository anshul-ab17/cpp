// LC 42. Trapping Rain Water | Hard
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& h) {
        int l = 0, r = h.size() - 1, lmax = 0, rmax = 0, res = 0;
        while (l <= r) {
            if (lmax <= rmax) { lmax = max(lmax, h[l]); res += lmax - h[l++]; }
            else { rmax = max(rmax, h[r]); res += rmax - h[r--]; }
        }
        return res;
    }
};
