// LC 19. Remove Nth Node From End of List | Medium
struct ListNode { int val; ListNode* next; ListNode(int x, ListNode* n = nullptr) : val(x), next(n) {} };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0, head);
        ListNode *slow = &dummy, *fast = &dummy;
        for (int i = 0; i <= n; i++) fast = fast->next;
        while (fast) { slow = slow->next; fast = fast->next; }
        slow->next = slow->next->next;
        return dummy.next;
    }
};
