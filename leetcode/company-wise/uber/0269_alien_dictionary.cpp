// LC 269. Alien Dictionary | Hard | Uber, Google
#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, unordered_set<char>> adj;
        unordered_map<char, int> indeg;
        for (auto& w : words) for (char c : w) indeg[c] = 0;
        for (int i = 0; i < (int)words.size()-1; i++) {
            string &w1 = words[i], &w2 = words[i+1];
            int mn = min(w1.size(), w2.size());
            if (w1.size() > w2.size() && w1.substr(0,mn) == w2.substr(0,mn)) return "";
            for (int j = 0; j < mn; j++)
                if (w1[j] != w2[j]) { if (!adj[w1[j]].count(w2[j])) { adj[w1[j]].insert(w2[j]); indeg[w2[j]]++; } break; }
        }
        queue<char> q; for (auto& [c, d] : indeg) if (d == 0) q.push(c);
        string res;
        while (!q.empty()) { char c = q.front(); q.pop(); res += c; for (char n : adj[c]) if (--indeg[n]==0) q.push(n); }
        return res.size() == indeg.size() ? res : "";
    }
};
