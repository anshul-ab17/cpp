# LC 234. Palindrome Linked List | Easy
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

class Solution:
    def isPalindrome_brute(self, head):
        vals = []
        while head: vals.append(head.val); head = head.next
        return vals == vals[::-1]

    # O(1) space: find mid, reverse second half, compare
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next: slow = slow.next; fast = fast.next.next
        prev = None
        while slow: nxt = slow.next; slow.next = prev; prev = slow; slow = nxt
        while prev:
            if head.val != prev.val: return False
            head = head.next; prev = prev.next
        return True
