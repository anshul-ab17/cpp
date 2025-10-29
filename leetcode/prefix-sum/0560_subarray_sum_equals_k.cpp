// LC 560. Subarray Sum Equals K | Medium
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp{{0, 1}};
        int count = 0, cur = 0;
        for (int n : nums) {
            cur += n;
            count += mp[cur - k];
            mp[cur]++;
        }
        return count;
    }
};
