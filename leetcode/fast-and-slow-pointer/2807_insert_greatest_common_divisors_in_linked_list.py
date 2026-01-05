from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head):
        cur = head
        while cur and cur.next:
            cur.next = ListNode(gcd(cur.val, cur.next.val), cur.next)
            cur = cur.next.next
        return head
