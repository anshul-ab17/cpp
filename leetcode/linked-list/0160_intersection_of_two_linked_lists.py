class Solution:
    def getIntersectionNode(self, a, b):
        p1, p2 = a, b
        while p1 != p2:
            p1 = p1.next if p1 else b
            p2 = p2.next if p2 else a
        return p1
