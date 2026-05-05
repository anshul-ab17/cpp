// LC 787. Cheapest Flights Within K Stops | Medium (DP on Graph / Bellman-Ford)
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> prices(n, 1e9); prices[src] = 0;
        for (int i = 0; i <= k; i++) {
            vector<int> tmp = prices;
            for (auto& f : flights)
                if (prices[f[0]] < 1e9) tmp[f[1]] = min(tmp[f[1]], prices[f[0]]+f[2]);
            prices = tmp;
        }
        return prices[dst] >= 1e9 ? -1 : prices[dst];
    }
};
