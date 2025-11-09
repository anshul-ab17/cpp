// LC 528. Random Pick with Weight | Medium | Meta
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    vector<int> prefix;
public:
    Solution(vector<int>& w) : prefix(w) {
        for (int i = 1; i < w.size(); i++) prefix[i] += prefix[i-1];
    }
    int pickIndex() {
        int target = rand() % prefix.back();
        return upper_bound(prefix.begin(), prefix.end(), target) - prefix.begin();
    }
};
