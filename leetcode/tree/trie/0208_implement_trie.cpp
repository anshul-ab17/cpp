// LC 208. Implement Trie | Medium
#include <string>
using namespace std;

class Trie {
    struct Node { Node* ch[26] = {}; bool end = false; };
    Node* root;
    Node* find(string& s) {
        Node* n = root;
        for (char c : s) { if (!n->ch[c-'a']) return nullptr; n = n->ch[c-'a']; }
        return n;
    }
public:
    Trie() : root(new Node()) {}
    void insert(string word) {
        Node* n = root;
        for (char c : word) { if (!n->ch[c-'a']) n->ch[c-'a'] = new Node(); n = n->ch[c-'a']; }
        n->end = true;
    }
    bool search(string word) { Node* n = find(word); return n && n->end; }
    bool startsWith(string prefix) { return find(prefix) != nullptr; }
};
