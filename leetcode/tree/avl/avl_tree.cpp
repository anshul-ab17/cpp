// AVL Tree Implementation
#include <algorithm>
#include <cassert>
using namespace std;

struct Node {
    int key, height; Node *left, *right;
    Node(int k) : key(k), height(1), left(nullptr), right(nullptr) {}
};

class AVLTree {
    int h(Node* n) { return n ? n->height : 0; }
    void upd(Node* n) { n->height = 1 + max(h(n->left), h(n->right)); }
    Node* rotR(Node* y) { Node* x = y->left; y->left = x->right; x->right = y; upd(y); upd(x); return x; }
    Node* rotL(Node* x) { Node* y = x->right; x->right = y->left; y->left = x; upd(x); upd(y); return y; }
public:
    Node* insert(Node* n, int key) {
        if (!n) return new Node(key);
        if (key < n->key) n->left = insert(n->left, key);
        else if (key > n->key) n->right = insert(n->right, key);
        else return n;
        upd(n); int b = h(n->left) - h(n->right);
        if (b > 1 && key < n->left->key) return rotR(n);
        if (b < -1 && key > n->right->key) return rotL(n);
        if (b > 1 && key > n->left->key) { n->left = rotL(n->left); return rotR(n); }
        if (b < -1 && key < n->right->key) { n->right = rotR(n->right); return rotL(n); }
        return n;
    }
};

int main() {
    AVLTree avl; Node* root = nullptr;
    for (int k : {10,20,30,40,50,25}) root = avl.insert(root, k);
    return 0;
}
