# LC 138. Copy List with Random Pointer | Medium | Amazon
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x; self.next = next; self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return None
        old_to_new = {}
        cur = head
        while cur: old_to_new[cur] = Node(cur.val); cur = cur.next
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]
