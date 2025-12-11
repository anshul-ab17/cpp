# LC 206. Reverse Linked List | Easy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

class Solution:
    # Iterative - O(n) time, O(1) space
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next; curr.next = prev; prev = curr; curr = nxt
        return prev

    # Recursive
    def reverseList_rec(self, head):
        if not head or not head.next: return head
        new_head = self.reverseList_rec(head.next)
        head.next.next = head; head.next = None
        return new_head
