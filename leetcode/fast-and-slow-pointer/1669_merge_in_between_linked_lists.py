# Find nodes a-1 and b+1 using traversal and reconnect lists.
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        before = list1
        for _ in range(a - 1):
            before = before.next

        after = before
        for _ in range(b - a + 2):
            after = after.next

        before.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after

        return list1
