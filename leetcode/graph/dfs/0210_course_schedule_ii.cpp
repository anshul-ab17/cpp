// LC 210. Course Schedule II | Medium (Topological Sort)
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& pre) {
        vector<vector<int>> g(n); vector<int> indeg(n, 0);
        for (auto& p : pre) { g[p[1]].push_back(p[0]); indeg[p[0]]++; }
        queue<int> q; for (int i = 0; i < n; i++) if (!indeg[i]) q.push(i);
        vector<int> order;
        while (!q.empty()) {
            int u = q.front(); q.pop(); order.push_back(u);
            for (int v : g[u]) if (--indeg[v] == 0) q.push(v);
        }
        return order.size() == n ? order : vector<int>();
    }
};
