// LC 438. Find All Anagrams in a String | Medium
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if (p.size() > s.size()) return {};
        vector<int> res, pc(26, 0), sc(26, 0);
        for (int i = 0; i < p.size(); i++) { pc[p[i]-'a']++; sc[s[i]-'a']++; }
        if (pc == sc) res.push_back(0);
        for (int i = p.size(); i < s.size(); i++) {
            sc[s[i]-'a']++; sc[s[i-p.size()]-'a']--;
            if (pc == sc) res.push_back(i - p.size() + 1);
        }
        return res;
    }
};
