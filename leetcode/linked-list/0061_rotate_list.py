class Solution:
    def rotateRight(self, head, k):
        if not head: return head
        n, tail = 1, head
        while tail.next:
            tail = tail.next; n += 1
        k %= n
        if k == 0: return head
        tail.next = head
        for _ in range(n - k):
            tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead
