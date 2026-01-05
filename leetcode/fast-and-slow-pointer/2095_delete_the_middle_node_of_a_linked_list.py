class Solution:
    def deleteMiddle(self, head):
        if not head.next:
            return None

        slow, fast = head, head.next.next
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next
        else:
            head = head.next

        return head
