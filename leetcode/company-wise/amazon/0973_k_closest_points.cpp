// LC 973. K Closest Points to Origin | Medium | Amazon
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto cmp = [](vector<int>& a, vector<int>& b) {
            return a[0]*a[0]+a[1]*a[1] < b[0]*b[0]+b[1]*b[1];
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> pq(cmp);
        for (auto& p : points) { pq.push(p); if (pq.size() > k) pq.pop(); }
        vector<vector<int>> res;
        while (!pq.empty()) { res.push_back(pq.top()); pq.pop(); }
        return res;
    }
};
