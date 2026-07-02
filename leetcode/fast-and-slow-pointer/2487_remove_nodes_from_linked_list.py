# Reverse list -> remove smaller nodes -> reverse again.
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class Solution:
    def removeNodes(self, head):
        def reverse(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        head = reverse(head)
        max_so_far = head.val
        node = head
        while node.next:
            if node.next.val < max_so_far:
                node.next = node.next.next
            else:
                node = node.next
                max_so_far = node.val

        return reverse(head)
