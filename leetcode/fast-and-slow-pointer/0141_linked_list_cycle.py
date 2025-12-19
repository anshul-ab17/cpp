# LC 141. Linked List Cycle | Easy
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class Solution:
    # Hash set - O(n) space
    def hasCycle_brute(self, head):
        seen = set()
        while head:
            if head in seen: return True
            seen.add(head); head = head.next
        return False

    # Floyd's - O(1) space
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next; fast = fast.next.next
            if slow == fast: return True
        return False
