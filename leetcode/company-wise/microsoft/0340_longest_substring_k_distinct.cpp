// LC 340. Longest Substring with At Most K Distinct Characters | Medium | Microsoft
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int> cnt; int l = 0, res = 0;
        for (int r = 0; r < s.size(); r++) {
            cnt[s[r]]++;
            while (cnt.size() > k) { if (--cnt[s[l]] == 0) cnt.erase(s[l]); l++; }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
