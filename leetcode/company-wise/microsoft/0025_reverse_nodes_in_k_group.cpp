// LC 25. Reverse Nodes in k-Group | Hard | Microsoft
struct ListNode { int val; ListNode* next; ListNode(int x) : val(x), next(nullptr) {} };

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* node = head; int cnt = 0;
        while (node && cnt < k) { node = node->next; cnt++; }
        if (cnt < k) return head;
        ListNode *prev = nullptr, *curr = head;
        for (int i = 0; i < k; i++) { ListNode* nxt = curr->next; curr->next = prev; prev = curr; curr = nxt; }
        head->next = reverseKGroup(curr, k);
        return prev;
    }
};
