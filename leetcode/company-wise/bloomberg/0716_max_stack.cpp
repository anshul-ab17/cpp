// LC 716. Max Stack | Hard | Bloomberg
#include <list>
#include <map>
#include <stack>
using namespace std;

class MaxStack {
    list<int> dll;
    map<int, vector<list<int>::iterator>> mp;
public:
    void push(int x) { dll.push_back(x); mp[x].push_back(prev(dll.end())); }
    int pop() {
        int val = dll.back(); dll.pop_back();
        mp[val].pop_back(); if (mp[val].empty()) mp.erase(val);
        return val;
    }
    int top() { return dll.back(); }
    int peekMax() { return mp.rbegin()->first; }
    int popMax() {
        int val = mp.rbegin()->first;
        auto it = mp[val].back(); mp[val].pop_back();
        if (mp[val].empty()) mp.erase(val);
        dll.erase(it); return val;
    }
};
