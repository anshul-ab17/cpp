// LC 5. Longest Palindromic Substring | Medium
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, maxLen = 0, n = s.size();
        auto expand = [&](int l, int r) {
            while (l >= 0 && r < n && s[l] == s[r]) { l--; r++; }
            if (r-l-1 > maxLen) { start = l+1; maxLen = r-l-1; }
        };
        for (int i = 0; i < n; i++) { expand(i,i); expand(i,i+1); }
        return s.substr(start, maxLen);
    }
};
