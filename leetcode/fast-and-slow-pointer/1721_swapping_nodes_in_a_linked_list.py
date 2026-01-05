class Solution:
    def swapNodes(self, head, k):
        first = head
        for _ in range(k - 1):
            first = first.next

        slow, fast = head, first
        while fast.next:
            slow = slow.next
            fast = fast.next

        first.val, slow.val = slow.val, first.val
        return head
