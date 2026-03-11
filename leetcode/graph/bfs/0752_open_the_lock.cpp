// LC 752. Open the Lock | Medium
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end()), vis;
        if (dead.count("0000")) return -1;
        queue<pair<string,int>> q; q.push({"0000", 0}); vis.insert("0000");
        while (!q.empty()) {
            auto [state, turns] = q.front(); q.pop();
            if (state == target) return turns;
            for (int i = 0; i < 4; i++)
                for (int d : {1, -1}) {
                    string nxt = state; nxt[i] = '0' + (nxt[i]-'0'+d+10)%10;
                    if (!vis.count(nxt) && !dead.count(nxt)) { vis.insert(nxt); q.push({nxt, turns+1}); }
                }
        }
        return -1;
    }
};
