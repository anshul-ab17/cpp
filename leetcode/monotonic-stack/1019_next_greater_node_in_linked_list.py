# Convert linked list to array then apply NGE.
class ListNode:
    def __init__(self, x):
        self.val = x; self.next = None

class Solution:
    def nextLargerNodes(self, head):
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        res = [0] * len(vals)
        stack = []
        for i, v in enumerate(vals):
            while stack and vals[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(i)

        return res
