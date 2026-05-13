// B-Tree (order 3) - simplified insert
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

struct BNode {
    vector<int> keys; vector<BNode*> ch; bool leaf;
    BNode(bool l=true) : leaf(l) {}
};

class BTree {
    int t;
    void split(BNode* p, int i) {
        BNode* y = p->ch[i]; BNode* z = new BNode(y->leaf);
        p->keys.insert(p->keys.begin()+i, y->keys[t-1]);
        p->ch.insert(p->ch.begin()+i+1, z);
        z->keys.assign(y->keys.begin()+t, y->keys.end());
        y->keys.resize(t-1);
        if (!y->leaf) { z->ch.assign(y->ch.begin()+t, y->ch.end()); y->ch.resize(t); }
    }
    void insertNonFull(BNode* x, int k) {
        if (x->leaf) { x->keys.push_back(k); sort(x->keys.begin(), x->keys.end()); return; }
        int i = x->keys.size()-1;
        while (i >= 0 && k < x->keys[i]) i--;
        i++;
        if ((int)x->ch[i]->keys.size() == 2*t-1) { split(x, i); if (k > x->keys[i]) i++; }
        insertNonFull(x->ch[i], k);
    }
public:
    BNode* root;
    BTree(int t=2) : t(t), root(new BNode()) {}
    void insert(int k) {
        if ((int)root->keys.size() == 2*t-1) {
            BNode* s = new BNode(false); s->ch.push_back(root);
            split(s, 0); root = s;
        }
        insertNonFull(root, k);
    }
};

int main() { BTree bt(2); for (int k : {10,20,5,6,12,30,7,17}) bt.insert(k); printf("B-Tree OK\n"); }
