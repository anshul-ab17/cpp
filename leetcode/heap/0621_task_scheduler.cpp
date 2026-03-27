// LC 621. Task Scheduler | Medium
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int freq[26] = {};
        for (char c : tasks) freq[c-'A']++;
        int maxF = *max_element(freq, freq+26);
        int maxCnt = count(freq, freq+26, maxF);
        return max((int)tasks.size(), (maxF-1)*(n+1)+maxCnt);
    }
};
