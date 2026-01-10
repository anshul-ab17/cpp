// LC 150. Evaluate Reverse Polish Notation | Medium
#include <vector>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<long long> st;
        for (auto& t : tokens) {
            if (t == "+" || t == "-" || t == "*" || t == "/") {
                long long b = st.top(); st.pop(); long long a = st.top(); st.pop();
                if (t == "+") st.push(a+b); else if (t == "-") st.push(a-b);
                else if (t == "*") st.push(a*b); else st.push(a/b);
            } else st.push(stoll(t));
        }
        return st.top();
    }
};
