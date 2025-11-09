# LC 25. Reverse Nodes in k-Group | Hard | Microsoft
class ListNode:
    def __init__(self, val=0, next=None): self.val = val; self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k: node = node.next; count += 1
        if count < k: return head
        prev, curr = None, head
        for _ in range(k): nxt = curr.next; curr.next = prev; prev = curr; curr = nxt
        head.next = self.reverseKGroup(curr, k)
        return prev
