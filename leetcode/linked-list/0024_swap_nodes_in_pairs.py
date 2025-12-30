class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next, b.next, a.next = b, a, b.next
            cur = a
        return dummy.next
