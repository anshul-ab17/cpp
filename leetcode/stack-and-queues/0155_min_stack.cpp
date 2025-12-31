// LC 155. Min Stack | Medium
#include <stack>
using namespace std;

class MinStack {
    stack<int> st, minSt;
public:
    void push(int val) { st.push(val); minSt.push(minSt.empty() ? val : min(val, minSt.top())); }
    void pop() { st.pop(); minSt.pop(); }
    int top() { return st.top(); }
    int getMin() { return minSt.top(); }
};
