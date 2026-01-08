// LC 739. Daily Temperatures | Medium
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temp) {
        int n = temp.size();
        vector<int> res(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && temp[st.top()] < temp[i]) { res[st.top()] = i - st.top(); st.pop(); }
            st.push(i);
        }
        return res;
    }
};
