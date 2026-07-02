# Use slow/fast pointer to split linked list for merge sort.
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self._merge(left, right)

    def _merge(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
