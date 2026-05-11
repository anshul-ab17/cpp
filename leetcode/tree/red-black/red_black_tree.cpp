// Red-Black Tree - Simplified Insert Only
#include <cstdio>
enum Color { RED, BLACK };
struct Node {
    int key; Color color; Node *left, *right, *parent;
    Node(int k, Color c = RED) : key(k), color(c), left(nullptr), right(nullptr), parent(nullptr) {}
};

class RBTree {
    Node* nil;
    void leftRotate(Node* x) {
        Node* y = x->right; x->right = y->left;
        if (y->left != nil) y->left->parent = x;
        y->parent = x->parent;
        if (x->parent == nil) root = y;
        else if (x == x->parent->left) x->parent->left = y;
        else x->parent->right = y;
        y->left = x; x->parent = y;
    }
    void rightRotate(Node* y) {
        Node* x = y->left; y->left = x->right;
        if (x->right != nil) x->right->parent = y;
        x->parent = y->parent;
        if (y->parent == nil) root = x;
        else if (y == y->parent->right) y->parent->right = x;
        else y->parent->left = x;
        x->right = y; y->parent = x;
    }
    void fixInsert(Node* z) {
        while (z->parent->color == RED) {
            if (z->parent == z->parent->parent->left) {
                Node* y = z->parent->parent->right;
                if (y->color == RED) { z->parent->color = y->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent; }
                else { if (z == z->parent->right) { z = z->parent; leftRotate(z); }
                    z->parent->color = BLACK; z->parent->parent->color = RED; rightRotate(z->parent->parent); }
            } else {
                Node* y = z->parent->parent->left;
                if (y->color == RED) { z->parent->color = y->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent; }
                else { if (z == z->parent->left) { z = z->parent; rightRotate(z); }
                    z->parent->color = BLACK; z->parent->parent->color = RED; leftRotate(z->parent->parent); }
            }
        }
        root->color = BLACK;
    }
public:
    Node* root;
    RBTree() : nil(new Node(0, BLACK)) { root = nil; }
    void insert(int key) {
        Node* z = new Node(key); z->left = z->right = z->parent = nil;
        Node* p = nil; Node* c = root;
        while (c != nil) { p = c; c = key < c->key ? c->left : c->right; }
        z->parent = p;
        if (p == nil) root = z;
        else if (key < p->key) p->left = z;
        else p->right = z;
        fixInsert(z);
    }
};

int main() { RBTree t; for (int k : {7,3,18,10,22,8,11,26}) t.insert(k); printf("RB Tree OK\n"); }
