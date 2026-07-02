# Use slow pointer to find middle node as root.
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x; self.left = None; self.right = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
