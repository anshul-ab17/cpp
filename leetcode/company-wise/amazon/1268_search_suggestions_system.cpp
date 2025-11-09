// LC 1268. Search Suggestions System | Medium | Amazon
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(), products.end());
        vector<vector<string>> res; string prefix;
        for (char c : searchWord) {
            prefix += c;
            auto it = lower_bound(products.begin(), products.end(), prefix);
            vector<string> matches;
            for (int i = 0; i < 3 && it + i != products.end(); i++) {
                if ((it+i)->substr(0, prefix.size()) == prefix) matches.push_back(*(it+i));
                else break;
            }
            res.push_back(matches);
        }
        return res;
    }
};
