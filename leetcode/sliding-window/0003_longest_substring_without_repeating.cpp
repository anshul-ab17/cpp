// LC 3. Longest Substring Without Repeating Characters | Medium
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen;
        int l = 0, res = 0;
        for (int r = 0; r < s.size(); r++) {
            if (seen.count(s[r]) && seen[s[r]] >= l)
                l = seen[s[r]] + 1;
            seen[s[r]] = r;
            res = max(res, r - l + 1);
        }
        return res;
    }
};
