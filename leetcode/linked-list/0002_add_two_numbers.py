# LC 2. Add Two Numbers | Medium
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(); curr, carry = dummy, 0
        while l1 or l2 or carry:
            s = carry
            if l1: s += l1.val; l1 = l1.next
            if l2: s += l2.val; l2 = l2.next
            curr.next = ListNode(s % 10); carry = s // 10; curr = curr.next
        return dummy.next
