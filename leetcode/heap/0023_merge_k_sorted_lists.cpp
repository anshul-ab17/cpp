// LC 23. Merge k Sorted Lists | Hard
#include <vector>
#include <queue>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int x) : val(x), next(nullptr) {} };

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
        for (auto* l : lists) if (l) pq.push(l);
        ListNode dummy(0); ListNode* cur = &dummy;
        while (!pq.empty()) {
            cur->next = pq.top(); pq.pop(); cur = cur->next;
            if (cur->next) pq.push(cur->next);
        }
        return dummy.next;
    }
};
