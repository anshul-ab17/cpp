// Min Heap Implementation
#include <vector>
#include <cassert>
using namespace std;

class MinHeap {
    vector<int> h;
    void up(int i) { while (i > 0) { int p = (i-1)/2; if (h[i] < h[p]) swap(h[i], h[p]); i = p; } }
    void down(int i) {
        int n = h.size();
        while (2*i+1 < n) { int ch = 2*i+1; if (ch+1<n && h[ch+1]<h[ch]) ch++; if (h[i]<=h[ch]) break; swap(h[i],h[ch]); i=ch; }
    }
public:
    void push(int v) { h.push_back(v); up(h.size()-1); }
    int pop() { int v = h[0]; h[0] = h.back(); h.pop_back(); if (!h.empty()) down(0); return v; }
};

int main() { MinHeap h; for (int v : {5,3,8,1,2}) h.push(v); assert(h.pop()==1); assert(h.pop()==2); }
