// LC 138. Copy List with Random Pointer | Medium | Amazon
#include <unordered_map>
using namespace std;

class Node { public: int val; Node* next; Node* random;
    Node(int _val) : val(_val), next(nullptr), random(nullptr) {} };

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;
        unordered_map<Node*, Node*> mp;
        Node* cur = head;
        while (cur) { mp[cur] = new Node(cur->val); cur = cur->next; }
        cur = head;
        while (cur) { mp[cur]->next = mp[cur->next]; mp[cur]->random = mp[cur->random]; cur = cur->next; }
        return mp[head];
    }
};
