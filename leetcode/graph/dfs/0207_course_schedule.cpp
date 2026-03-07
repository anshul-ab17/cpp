// LC 207. Course Schedule | Medium
#include <vector>
using namespace std;

class Solution {
    bool dfs(vector<vector<int>>& g, vector<int>& st, int node) {
        if (st[node] == 1) return false;
        if (st[node] == 2) return true;
        st[node] = 1;
        for (int nei : g[node]) if (!dfs(g, st, nei)) return false;
        st[node] = 2; return true;
    }
public:
    bool canFinish(int n, vector<vector<int>>& pre) {
        vector<vector<int>> g(n);
        for (auto& p : pre) g[p[0]].push_back(p[1]);
        vector<int> st(n, 0);
        for (int i = 0; i < n; i++) if (!dfs(g, st, i)) return false;
        return true;
    }
};
